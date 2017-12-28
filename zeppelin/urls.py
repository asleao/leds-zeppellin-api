from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register('tools', viewsets.ToolViewSet)
router.register('languages', viewsets.LanguageViewSet)
router.register('projects', viewsets.ProjectViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
