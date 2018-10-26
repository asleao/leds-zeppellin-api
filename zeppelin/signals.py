from .models import Project, Language, ToolCredential
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .message import *
import json
from django.contrib.auth.models import User


@receiver(m2m_changed, sender=Project.team.through)
def send_project_to_queue(sender, instance, **kwargs):
    """
        Function responsible for sending a json with a project object to the queue.
    """
    # TODO: verificar uma maneira melhor de converter esse json.

    team = [team.username for team in instance.team.all()]

    if(team):
        data = {}
        data['name'] = instance.name
        data['tools'] = {}
        data['tools'] = [tool.name for tool in instance.tools.all()]
        data['team'] = {}
        data['team'] = team
        data['language'] = instance.language.name

        # TODO: Buscar as credenciais do owner.
        credential = ToolCredential.objects.get(owner=instance.owner, tool=1)
        data['token'] = credential.token
        
        message = Message(queue="Github", exchange='',
                          routing_key="Github", body=json.dumps(data))
        message.send_message()
