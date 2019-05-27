from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .base import UserMixinTestCase


class UserProfileTestCase(UserMixinTestCase, TestCase):

    def test_anon(self):
        # WHEN anon user visit the user profile
        response = self.client.get(reverse('user_profile'))

        # THEN the the user get a 302 to redirect to login
        self.assertEqual(response.status_code, 302)

    def test_user_profile_access(self):
        # GIVEN a logged in user:
        user = self.create_user()
        self.login_user(user)

        # WHEN user access his profile
        response = self.client.get(reverse('user_profile'))

        # THEN the user see the page
        self.assertEqual(response.status_code, 200)

    def test_user_profile_update(self):
        # GIVEN a logged in user:
        user = self.create_user()
        self.login_user(user)

        # WHEN user update his profile
        response = self.client.post(
            reverse('user_profile'),
            {
                'first_name': 'Juan',
                'last_name': 'Tanamera',
                'birthday': '1983-10-03',
                'phone': '0303-456',
                'language': 'es',
            }
        )

        # THEN the user is updated
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Juan')
        self.assertEqual(user.last_name, 'Tanamera')
        self.assertEqual(user.phone, '0303-456')
