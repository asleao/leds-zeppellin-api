from django.db import models
from django.contrib.auth.models import User


class Tool(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    authorization_url = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    tools = models.ManyToManyField(Tool, related_name='tools')
    team = models.ManyToManyField(User, related_name='team')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')

    def __str__(self):
        return self.name

class ToolCredential(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    token = models.CharField(max_length=150, blank=True, unique=True) # Encryptar o token

    def __str__(self):
        return self.tool.name