from django.test import TestCase
from django.urls import reverse
from mock import patch

from .base import UserMixinTestCase


class LandingPageTestCase(UserMixinTestCase, TestCase):

    def test_root_landing_page_anon(self):
        # WHEN root page is visited by anon user
        response = self.client.get('/', follow=True)

        # THEN the the user is redirected to the login page and next page is user home
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[-1][0],
            '{}?next={}'.format(reverse('account_login'), reverse('user_home'))
        )

    def test_fe_landing_page_anon(self):
        # WHEN landing page is visited by anon user
        landing_url = reverse('user_home')
        response = self.client.get(landing_url)

        # THEN the the user is redirected to the login page
        self.assertRedirects(
            response,
            '{}?next={}'.format(reverse('account_login'), landing_url),
            status_code=302
        )

    @patch('user.views.UserHomeView.template_name', 'user/test_index.html')
    def test_fe_landing_page(self):
        # GIVEN a logged in user:
        user = self.create_user()
        self.login_user(user)

        # WHEN landing page is visited
        landing_url = reverse('user_home')
        response = self.client.get(landing_url)

        # THEN the the user see the angular page app
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Odogram')
        self.assertContains(response, '<app-root>')
