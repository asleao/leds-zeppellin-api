import factory

from languages.models import Language


class LanguageFactory(factory.Factory):
    class Meta:
        model = Language

    name = factory.Faker('name')
