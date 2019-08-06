import os

from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from projects.views import send_messages, collaborator_messages, tool_messages
from tools.models import Tool
from .models import Project, ToolSignalData, CollaboratorSignalData


@receiver(m2m_changed, sender=Project.tools.through)
def send_project_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a the project to all queues.
    """

    action = kwargs['action'].split('_')

    if action[0] == 'post':
        set_tools = kwargs['pk_set']
        queue_sufix = os.environ.get('PROJECT_QUEUE')
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
        queue_sufix = os.environ.get('COLLABORATOR_QUEUE')
        collaborators = User.objects.filter(pk__in=set_collaborators)
        messages = collaborator_messages(CollaboratorSignalData(instance, action[1], collaborators))
        send_messages(queue_sufix, messages)
