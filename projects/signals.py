from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from tools.models import ToolCredential, Tool
from .models import Project, ToolMessage, ToolSignalData, CollaboratorSignalData, CollaboratorMessage


@receiver(m2m_changed, sender=Project.tools.through)
def send_project_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a the project to all queues.
    """

    action = kwargs['action'].split('_')

    if action[0] == 'post':
        set_tools = kwargs['pk_set']
        queue_sufix = "Repository"
        tools = Tool.objects.filter(pk__in=set_tools)
        messages = tool_messages(ToolSignalData(instance, action[1], tools))
        send_messages(queue_sufix, messages)


@receiver(m2m_changed, sender=Project.team.through)
def send_team_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a team of a project to the queue.
    """
    action = kwargs['action'].split('_')

    if action[0] == 'post':
        set_collaborators = kwargs['pk_set']
        queue_sufix = "Collaborator"
        collaborators = User.objects.filter(pk__in=set_collaborators)
        messages = collaborator_messages(CollaboratorSignalData(instance, action[1], collaborators))
        send_messages(queue_sufix, messages)


def collaborator_messages(signal_data):
    messages = []
    for collaborator in signal_data.collaborators:
        for tool in signal_data.instance.tools.all():
            credential = ToolCredential.objects.get(owner=signal_data.instance.owner, tool=tool)
            message = CollaboratorMessage(signal_data.instance.language.name, signal_data.instance.name,
                                          signal_data.action, tool.name, collaborator, credential.token)
            messages.append(message)
    return messages


def tool_messages(signal_data):
    messages = []
    for tool in signal_data.tools:
        message = ToolMessage(signal_data.instance.language.name, signal_data.instance.name, signal_data.action,
                              tool.name)
        messages.append(message)
    return messages


def send_messages(queue_sufix, messages):
    for message in messages:
        message.message(queue_sufix).send_message()
