from django.test import TestCase
from django.urls import reverse_lazy
from .models import User


First_user = {
    'username': 'firstuser',
    'password': 'Один',
    }

Second_user = {
    'username': 'secondtuser',
    'first_name': 'Second',
    'last_name': 'Второй',
    'password1': 'Два',
    'password2': 'Два'
    }


class UsersTest(TestCase):
    url_register = reverse_lazy('create_user')
    url_login = reverse_lazy('log_in')
    url_user_update = reverse_lazy('user_update', args=[1])
    url_user_delete = reverse_lazy('user_delete', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(**First_user)

    def test_user_register(self):
        initial_users_count = User.objects.count()
        self.client.post(
            self.url_register, data=Second_user
            )
        self.assertEqual(
            User.objects.count(), initial_users_count + 1
            )

    def test_user_login(self):
        self.client.post(self.url_login, data=First_user)
        auth_id = self.client.session['_auth_user_id']
        self.assertEqual(
            User.objects.get(pk=auth_id).username, 'firstuser'
            )

    def test_user_update(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(self.url_user_update, data=Second_user)
        self.assertEqual(
            User.objects.get(pk=1).username, 'secondtuser'
            )

    def test_user_delete(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(self.url_user_delete)
        self.assertEqual(User.objects.count(), 0)
