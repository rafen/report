from django.urls import reverse
from django.utils.translation import get_language
from rest_framework import status
from rest_framework.test import APITestCase
from user.tests.base import UserMixinTestCase


class UserLanguageAPITest(UserMixinTestCase, APITestCase):

    def test_user_language_anon(self):
        # WHEN anon user visit the list endpoint
        response = self.client.get(reverse('api-user-language'))

        # THEN a 401 is returned
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_language_retrieve(self):
        # GIVEN a logged in user
        user = self.create_user()
        self.login_user(user)

        # WHEN user access by get the language endpoint
        response = self.client.get(reverse('api-user-language'))

        # THEN a 200 is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # AND the language of the user is returned
        self.assertEqual(response.json()['language'], user.language)

    def test_user_language_update(self):
        # GIVEN a logged in user
        user = self.create_user()
        self.login_user(user)

        # WHEN user access by get the language endpoint
        response = self.client.put(reverse('api-user-language'), {'language': 'en'})

        # THEN a 200 is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # AND the language of the user is returned
        self.assertEqual(response.json()['language'], 'en')
        # AND the user is updated
        user.refresh_from_db()
        self.assertEqual(user.language, 'en')
