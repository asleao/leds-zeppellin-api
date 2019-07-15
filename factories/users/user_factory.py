import factory
from django.contrib.auth.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
