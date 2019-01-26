import json
from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from django.db import models

from core.message import Message
from languages.models import Language
from tools.models import Tool


class Project(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    tools = models.ManyToManyField(Tool, related_name='tools')
    team = models.ManyToManyField(User, related_name='team')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')

    def __str__(self):
        return self.name

    def has_tools(self):
        return self.tools.exists()


class MessageQueue(ABC):

    def __init__(self, name, action, token, language):
        self.name = name
        self.action = action
        self.token = token
        self.language = language
        super(MessageQueue, self).__init__()

    @abstractmethod
    def message(self, queue_sufix):
        pass


class ToolMessage(MessageQueue):
    # TODO Verificar se tem como generalizar.
    def message(self, queue_sufix):
        return Message(queue=f"{self.tool}_{queue_sufix}", exchange='',
                       routing_key=f"{self.tool}_{queue_sufix}", body=json.dumps(self.__dict__))

    def __init__(self, name, action, token, language, tool):
        super().__init__(name, action, token, language)
        self.tool = tool


class CollaboratorMessage(ToolMessage):

    def __init__(self, name, action, token, tool, language, collaborator):
        super().__init__(name, action, token, language, tool)
        self.collaborator = collaborator


class SignalData(ABC):

    def __init__(self, instance, action):
        self.instance = instance
        self.action = action


class ToolSignalData(SignalData):

    def __init__(self, instance, action, tools):
        super().__init__(instance, action)
        self.tools = tools


class CollaboratorSignalData(SignalData):

    def __init__(self, instance, action, collaborators):
        super().__init__(instance, action)
        self.collaborators = collaborators
