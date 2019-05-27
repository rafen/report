from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from mock import patch

from .base import UserMixinTestCase


class AuthPageTestCase(UserMixinTestCase, TestCase):

    def test_login_page(self):
        # WHEN user visit the login page
        response = self.client.get(reverse('account_login'))

        # THEN the the user see page coorectly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Odogram')

    @patch('user.views.UserHomeView.template_name', 'user/test_index.html')
    def test_login_submit(self):
        # GIVEN a registered user
        email = 'john@example.com'
        password = 'secret'
        self.create_user(email=email, password=password)

        # WHEN user submit the login page
        response = self.client.post(
            reverse('account_login'),
            {'login': email, 'password': password}
        )

        # THEN the the user is redirected to the user home
        self.assertRedirects(
            response,
            reverse('user_home'),
            status_code=302
        )

    def test_signup_page(self):
        # WHEN user visit the login page
        response = self.client.get(reverse('account_signup'))

        # THEN the the user see page coorectly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Odogram')

    def test_signup_submit(self):
        # WHEN user submit the register page
        email = 'john@example.com'
        password = 'Secret17Odo'
        response = self.client.post(
            reverse('account_signup'),
            {
                'username': 'john',
                'email': email,
                'first_name': 'john',
                'last_name': 'Smith',
                'password1': password,
                'password2': password
            }
        )

        # THEN the the user is redirected to the user home
        self.assertRedirects(
            response,
            reverse('account_email_verification_sent'),
            status_code=302
        )
        # AND the user is on the DB
        user = get_user_model().objects.get()
        self.assertEqual(user.email, email)
