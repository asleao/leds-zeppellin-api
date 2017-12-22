from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register('tool', viewsets.ToolViewSet)
router.register('language', viewsets.LanguageViewSet)
router.register('project', viewsets.ProjectViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
