from django.test import TestCase
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth import get_user_model

New_user = {
    'username': 'secondtuser',
    'first_name': 'Second',
    'last_name': 'Второй',
    'password1': 'Два',
    'password2': 'Два'
}


class SetupUsersTest(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.user = get_user_model().objects.get(pk=1)
        self.url_register = reverse_lazy('create_user')
        self.url_login = reverse_lazy('log_in')
        self.url_user_update = reverse_lazy('user_update', args=[1])
        self.url_user_delete = reverse_lazy('user_delete', args=[1])


class TestUserRegister(SetupUsersTest):
    def test_user_register(self):
        initial_users_count = User.objects.count()
        self.client.post(
            self.url_register, data=New_user
        )
        self.assertEqual(
            User.objects.count(), initial_users_count + 1
        )

    def test_user_login(self):
        self.client.force_login(user=self.user)
        auth_id = self.client.session['_auth_user_id']
        self.assertEqual(
            User.objects.get(pk=auth_id).username, 'albert'
        )

    def test_user_update(self):
        self.client.force_login(user=self.user)
        self.client.post(self.url_user_update, data=New_user)
        self.assertEqual(
            User.objects.get(pk=1).username, 'secondtuser'
        )

    def test_user_delete(self):
        self.client.force_login(user=self.user)
        self.client.post(self.url_user_delete)
        self.assertEqual(User.objects.count(), 2)
