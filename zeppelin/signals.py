from .models import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from .message import *


@receiver(post_save, sender=Project)
def send_project_to_queue(sender, instance, **kwargs):
    message = Message(queue="Github", exchange='',
                      routing_key="Github", body="Teste")
    message.send_message()
