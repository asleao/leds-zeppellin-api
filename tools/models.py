from django.contrib.auth.models import User
from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=60, blank=False, unique=True)
    authorization_url = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class ToolCredential(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, unique=True)
    token = models.CharField(max_length=150, blank=True, unique=True)  # Encryptar o token

    def __str__(self):
        return self.tool.name

    @property
    def is_created(self):
        return self.token != ""
