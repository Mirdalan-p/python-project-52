from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.urls import reverse_lazy

First_user = {
    'username': 'firstuser',
    'password': 'Один'
    }


class SimpleTestCase(TestCase):
    url_login = reverse_lazy('log_in')
    url_create_label = reverse_lazy(
        'create_label')
    url_update_label = reverse_lazy(
        'label_update', kwargs={"pk": 1})
    url_delete_label = reverse_lazy(
        'label_delete', kwargs={"pk": 1})

    def setUp(self):
        self.user = User.objects.create_user(**First_user)

    def test_label_create(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_label, data={
                'name': 'first label'})
        response = self.client.get('/labels/')
        self.assertContains(response, "first label")

    def test_label_update(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_label, data={
                'name': 'first label'})
        self.client.post(
            self.url_update_label, data={
                'name': 'second label'})
        response = self.client.get('/labels/')
        self.assertNotContains(response, "first label")
        self.assertContains(response, "second label")

    def test_label_delete(self):
        self.client.post(self.url_login, data=First_user)
        self.client.post(
            self.url_create_label, data={
                'name': 'first label'})
        label = Label.objects.get(name='first label')
        self.client.post(self.url_delete_label, pk=label.id)
        response = self.client.get('/labels/')
        self.assertNotContains(response, "first label")
