from django.contrib.auth.models import Permission
from allauth.account.models import EmailAddress

from ..factories import UserFactory


class UserMixinTestCase(object):

    def create_user(self, username='John', email='john-qa@maillinator.com',
                    password='top_secret', permissions=[]):
        user = UserFactory.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        user.user_permissions.set(Permission.objects.filter(codename__in=permissions))
        EmailAddress.objects.create(user=user, email=email, verified=True, primary=True)
        return user

    def add_permission(self, user, permission):
        user.user_permissions.add(Permission.objects.get(codename=permission))

    def login_user(self, user):
        self.client.force_login(user)
