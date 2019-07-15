import factory

from tools.models import Tool


class ToolFactory(factory.Factory):
    class Meta:
        model = Tool

    name = factory.Faker('name')
