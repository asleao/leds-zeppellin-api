import json

from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from core.message import Message
from tools.models import ToolCredential, Tool
from .models import Project, ToolMessage, ToolSignalData


@receiver(m2m_changed, sender=Project.tools.through)
def send_project_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a the project to all queues.
    """

    action = kwargs['action'].split('_')

    if action[0] == 'post':
        set_tools = kwargs['pk_set']
        queue_sufix = "Repository"
        messages = tool_messages(ToolSignalData(instance, action[1], set_tools))
        send_messages(queue_sufix, messages)

@receiver(m2m_changed, sender=Project.team.through)
def send_team_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a team of a project to the queue.
    """
    action = kwargs['action'].split('_')

    if action[0] == 'post':
        data = {'name': instance.name, 'action': action[1]}

        credential = ToolCredential.objects.get(owner=instance.owner, tool=1)
        data['token'] = credential.token
        manage_collaborators(data, kwargs['pk_set'])


def manage_collaborators(data, set_collaborators):
    collaborators = []
    for primaryKey in set_collaborators:
        collaborators.append(User.objects.get(pk=primaryKey).username)
    data['collaborators'] = collaborators
    message = Message(queue="Github_Collaborator", exchange='',
                      routing_key="Github_Collaborator", body=json.dumps(data))
    message.send_message()


def tool_messages(signal_data):
    messages = []
    for tool_id in signal_data.set_tools:
        tool = Tool.objects.get(pk=tool_id)
        message = ToolMessage(signal_data.instance.language.name, signal_data.instance.name, signal_data.action,
                              tool.name)
        messages.append(message)
    return messages


def send_messages(queue_sufix, messages):
    for message in messages:
        message.message(queue_sufix).send_message()
