import factory

from factories.projects.project_factory import ProjectFactory
from projects.models import CollaboratorSignalData


class CollaboratorSignalDataFactory(factory.Factory):
    class Meta:
        model = CollaboratorSignalData

    instance = ProjectFactory()
