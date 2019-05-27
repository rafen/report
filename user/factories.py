import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'user{}@example.com'.format(n))
    email = factory.Sequence(lambda n: 'email{}@example.com'.format(n))
