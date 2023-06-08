from django.test import TestCase
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label
from django.urls import reverse_lazy


class SetupLabelsTest(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.user = get_user_model().objects.get(pk=1)
        self.url_login = reverse_lazy('log_in')
        self.url_labels_list = reverse_lazy(
            'labels_list'
        )
        self.url_create_label = reverse_lazy(
            'create_label')
        self.url_update_label = reverse_lazy(
            'label_update',
            kwargs={"pk": 1},
        )
        self.url_delete_label = reverse_lazy(
            'label_delete', kwargs={"pk": 1}
        )
        self.url_create_task = reverse_lazy(
            'create_task'
        )


class TestNoLoginLabelsViews(SetupLabelsTest):

    def test_open_labels_page_with_no_login(self):
        response = self.client.get(self.url_labels_list)
        self.assertEqual(response.status_code, 302)

    def test_open_create_label_page_with_no_login(self):
        response = self.client.get(self.url_create_label)
        self.assertEqual(response.status_code, 302)

    def test_open_update_label_page_with_no_login(self):
        response = self.client.get(self.url_update_label)
        self.assertEqual(response.status_code, 302)

    def test_open_delete_label_page_with_no_login(self):
        response = self.client.get(self.url_delete_label)
        self.assertEqual(response.status_code, 302)


class TestLabelCreate(SetupLabelsTest):
    fixtures = ['users.json', 'labels.json']

    def test_label_create(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            self.url_create_label, data={
                'name': 'new label'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response=response,
            expected_url=self.url_labels_list
        )
        label = Label.objects.get(name='new label')
        self.assertEqual(label.name, 'new label')


class TestLabelUpdate(SetupLabelsTest):
    fixtures = ['users.json', 'labels.json']

    def test_label_update(self):
        self.client.force_login(user=self.user)
        label = Label.objects.get(name="label 1")
        self.client.post(
            self.url_update_label,
            pk=label.id,
            data={
                'name': 'new label'})
        response = self.client.get(self.url_labels_list)
        self.assertNotContains(response, "label 1")
        self.assertContains(response, 'new label')


class TestLabelDelete(SetupLabelsTest):
    fixtures = ['users.json', 'labels.json']

    def test_label_delete(self):
        self.client.force_login(user=self.user)
        label = Label.objects.get(name='label 2')
        self.delete_label_url = reverse_lazy(
            'label_delete',
            kwargs={"pk": label.id}
        )
        response = self.client.delete(path=self.delete_label_url)
        self.assertEqual(first=response.status_code, second=302)
        self.assertRedirects(
            response=response,
            expected_url=self.url_labels_list
        )
        self.assertNotContains(
            self.client.get(self.url_labels_list),
            "label 2"
        )

    def test_delete_used_label(self):
        self.client.force_login(user=self.user)
        label = Label.objects.get(name='label 2')
        self.client.post(
            path=self.url_create_task,
            data={
                "name": "new task name",
                "description": "new task description",
                "status": 1,
                "labels": [2],
                "author": 1,
                "executor": 1
            }
        )
        response = self.client.delete(path=self.url_delete_label, pk=label.id)
        self.assertEqual(first=response.status_code, second=302)
        self.assertRedirects(
            response=response,
            expected_url=self.url_labels_list
        )
