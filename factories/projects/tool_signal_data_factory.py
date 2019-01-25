import factory

from factories.projects.project_factory import ProjectFactory
from projects.models import ToolSignalData


class ToolSignalDataFactory(factory.Factory):
    class Meta:
        model = ToolSignalData

    instance = ProjectFactory()
