import json

from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from core.message import Message
from tools.models import ToolCredential, Tool
from .models import Project


@receiver(m2m_changed, sender=Project.tools.through)
def send_project_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a the project to all queues.
    """
    # TODO: verificar uma maneira melhor de converter esse json.
    data = {'name': instance.name, 'language': instance.language.name, 'action': kwargs['action'].split('_')[1]}

    manage_tools(data, kwargs['pk_set'], instance.owner)


@receiver(m2m_changed, sender=Project.team.through)
def send_team_to_queue(instance, **kwargs):
    """
        Function responsible for sending a json with a team of a project to the queue.
    """
    # TODO: juntar com o metodo acima.
    data = {'name': instance.name, 'action': kwargs['action'].split('_')[1]}

    credential = ToolCredential.objects.get(owner=instance.owner, tool=1)
    data['token'] = credential.token
    if kwargs['action'] == "post_remove":
        data['action'] = "remove"
        manage_collaborators(data, kwargs['pk_set'])
    elif kwargs['action'] == "post_add":
        data['action'] = "add"
        manage_collaborators(data, kwargs['pk_set'])


def manage_collaborators(data, set_collaborators):
    collaborators = []
    for primaryKey in set_collaborators:
        collaborators.append(User.objects.get(pk=primaryKey).username)
    data['collaborators'] = collaborators
    message = Message(queue="Github_Collaborator", exchange='',
                      routing_key="Github_Collaborator", body=json.dumps(data))
    message.send_message()


def manage_tools(data, set_tools, owner):
    tools = []
    for primaryKey in set_tools:
        tools.append(Tool.objects.get(pk=primaryKey).name)
        credential = ToolCredential.objects.get(owner=owner, tool=primaryKey)
        data['token'] = credential.token
        message = Message(queue="Github_Repository", exchange='',
                          routing_key="Github_Repository", body=json.dumps(data))
        message.send_message()
