from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Tool)
admin.site.register(models.ToolCredential)
admin.site.register(models.Language)
admin.site.register(models.Project)
