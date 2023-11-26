from django.contrib.auth.models import User, Permission
from django.test import TestCase

API_ACCOUNTING_ACCOUNT = '/api/accounting/account/'

CREDENTIALS = {
    'username': 'user',
    'password': 'user'
}


class AccountTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(**CREDENTIALS, is_active=True)

    def test_authenticated_with_permission(self):
        # GIVEN
        self.user.user_permissions.set(Permission.objects.filter(codename__contains='_account'))
        self.user.save()
        self.client.login(**CREDENTIALS)
        # WHEN
        response = self.client.get(API_ACCOUNTING_ACCOUNT)
        # THEN
        self.assertEqual(200, response.status_code)

    def test_authenticated_without_permission(self):
        # GIVEN
        self.client.login(**CREDENTIALS)
        # WHEN
        response = self.client.get(API_ACCOUNTING_ACCOUNT)
        # THEN
        self.assertEqual(403, response.status_code)

    def test_unauthenticated(self):
        # WHEN
        response = self.client.get(API_ACCOUNTING_ACCOUNT)
        # THEN
        self.assertEqual(403, response.status_code)
