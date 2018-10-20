from .models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import json

@receiver(post_save, sender=Project)
def send_project_to_queue(sender, instance, **kwargs):
    print("Teste")
    #requests.post('https://leds-zeppellin-api.herokuapp.com/api/v1/projects/', data={'name': instance.name, 'tools': json.dumps(instance.tools), 'team': json.dumps(instance.team), 'owner':instance.owner,'language':instance.language})