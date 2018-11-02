from .models import Project, Language, ToolCredential, Tool
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .message import *
import json
from django.contrib.auth.models import User


@receiver(m2m_changed, sender=Project.tools.through)
def send_project_to_queue(sender, instance, **kwargs):
    """
        Function responsible for sending a json with a the project to all queues.
    """
    # TODO: verificar uma maneira melhor de converter esse json.
    # TODO: Fazer o envio para todas as ferramentas.
    data = {}
    data['name'] = instance.name
    credential = ToolCredential.objects.get(owner=instance.owner, tool=1)
    data['token'] = credential.token
    data['language'] = instance.language.name
    if kwargs['action'] == "post_remove":
        data['action'] = "remove"
        manage_tools(data, kwargs['pk_set'])
    elif kwargs['action'] == "post_add":
        data['action'] = "add"
        manage_tools(data, kwargs['pk_set'])


@receiver(m2m_changed, sender=Project.team.through)
def send_team_to_queue(sender, instance, **kwargs):
    """
        Function responsible for sending a json with a team of a project to the queue.
    """
    # TODO: verificar uma maneira melhor de converter esse json.
    data = {}
    data['name'] = instance.name
    credential = ToolCredential.objects.get(owner=instance.owner, tool=1)
    data['token'] = credential.token
    if kwargs['action'] == "post_remove":
        data['action'] = "remove"
        manage_collaborators(data, kwargs['pk_set'])
    elif kwargs['action'] == "post_add":
        data['action'] = "add"
        manage_collaborators(data, kwargs['pk_set'])
    print(data)


def manage_collaborators(data, set_collaborators):
    collaborators = []
    for primaryKey in set_collaborators:
        collaborators.append(User.objects.get(pk=primaryKey).username)
    data['collaborators'] = collaborators
    message = Message(queue="Github_Collaborator", exchange='',
                      routing_key="Github_Collaborator", body=json.dumps(data))
    message.send_message()


def manage_tools(data, set_tools):
    tools = []
    for primaryKey in set_tools:
        tools.append(Tool.objects.get(pk=primaryKey).name)
    message = Message(queue="Github_Repository", exchange='',
                      routing_key="Github_Repository", body=json.dumps(data))
    message.send_message()
