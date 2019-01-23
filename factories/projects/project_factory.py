import factory

from projects.models import Project


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    name = factory.Faker('first_name')
