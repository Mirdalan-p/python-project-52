from django.test import TestCase
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import ProtectedError


class SetupTestStatuses(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        self.user = get_user_model().objects.get(pk=1)
        self.url_login = reverse_lazy('log_in')
        self.url_statuses_list = reverse_lazy(
            'statuses_list'
        )
        self.url_create_status = reverse_lazy(
            'create_status')
        self.url_update_status = reverse_lazy(
            'status_update', kwargs={"pk": 1})
        self.url_delete_status = reverse_lazy(
            'status_delete', kwargs={"pk": 1})
        self.url_create_task = reverse_lazy(
            'create_task'
        )


class TestNoLoginStatusesViews(SetupTestStatuses):

    def test_open_statuses_page_with_no_login(self):
        response = self.client.get(self.url_statuses_list)
        self.assertEqual(response.status_code, 302)

    def test_open_create_status_page_with_no_login(self):
        response = self.client.get(self.url_create_status)
        self.assertEqual(response.status_code, 302)

    def test_open_update_status_page_with_no_login(self):
        response = self.client.get(self.url_update_status)
        self.assertEqual(response.status_code, 302)

    def test_open_delete_status_page_with_no_login(self):
        response = self.client.get(self.url_delete_status)
        self.assertEqual(response.status_code, 302)


class TestStatusCreate(SetupTestStatuses):
    fixtures = ["users.json", "statuses.json"]

    def test_status_create(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            self.url_create_status, data={
                'name': 'new status'
            }
        )
        self.assertRedirects(
            response=response, expected_url=self.url_statuses_list
        )
        self.assertEqual(response.status_code, 302)
        status = Status.objects.get(name='new status')
        self.assertEqual(status.name, 'new status')


class TestStatusUpdate(SetupTestStatuses):
    fixtures = ["users.json", "statuses.json"]

    def test_status_update(self):
        self.client.force_login(user=self.user)
        status = Status.objects.get(name="status 1",)
        self.client.post(
            self.url_update_status,
            pk=status.id,
            data={
                'name': 'new status'})
        response = self.client.get(self.url_statuses_list)
        self.assertNotContains(response, "status 1")
        self.assertContains(response, 'new status')


class TestStatusDelete(SetupTestStatuses):
    fixtures = ["users.json", "statuses.json"]

    def test_status_delete(self):
        self.client.force_login(user=self.user)
        status = Status.objects.get(name="status 1")
        self.delete_status_url = reverse_lazy(
            'status_delete', kwargs={"pk": status.id}
        )
        response = self.client.delete(path=self.delete_status_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response=response, expected_url=self.url_statuses_list
        )
        self.assertNotContains(
            self.client.get(self.url_statuses_list), "status 1"
        )

    def test_delete_used_status(self):
        self.client.force_login(user=self.user)
        self.client.post(
            self.url_create_status, data={
                'name': 'first status'})
        status = Status.objects.get(name="status 1")
        self.client.post(
            self.url_create_task,
            pk=status.id,
            data={
                "name": "new task name",
                "description": "new task description",
                "status": 1,
                "labels": [],
                "author": 1,
                "executor": 1
            }
        )
        with self.assertRaises(expected_exception=ProtectedError):
            response = self.client.post(self.url_delete_status, pk=status.id)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(
                response=response,
                expected_url=self.url_statuses_list
            )
