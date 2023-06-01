from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import User
from django.urls import reverse_lazy

First_user = {
    'username': 'firstuser',
    'password': 'Один'
}


class SimpleTestCase(TestCase):
    url_login = reverse_lazy('log_in')
    url_create_status = reverse_lazy(
        'create_status')
    url_update_status = reverse_lazy(
        'status_update', kwargs={"pk": 1})
    url_delete_status = reverse_lazy(
        'status_delete', kwargs={"pk": 1})

    def setUp(self):
        self.user = User.objects.create_user(**First_user)

    def test_status_create(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_status, data={
                'name': 'first status'})
        response = self.client.get('/statuses/')
        self.assertContains(response, "first status")

    def test_status_update(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_status, data={
                'name': 'first status'})
        self.client.post(
            self.url_update_status, data={
                'name': 'second status'})
        response = self.client.get('/statuses/')
        self.assertNotContains(response, "first status")
        self.assertContains(response, "second status")

    def test_status_delete(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_status, data={
                'name': 'first status'})
        status = Status.objects.get(name='first status')
        self.client.post(self.url_delete_status, pk=status.id)
        response = self.client.get('/statuses/')
        self.assertNotContains(response, "first status")
