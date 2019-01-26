import factory

from factories.languages.languages_factory import LanguageFactory
from projects.models import Project


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    name = factory.Faker('first_name')
    language = LanguageFactory()
