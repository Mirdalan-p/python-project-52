from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.tasks.models import Task


class SetupTestTasks(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def setUp(self):
        self.tasks_url = reverse_lazy('tasks_list')
        self.login_url = reverse_lazy('log_in')
        self.create_task_url = reverse_lazy('create_task')
        self.update_task_url = reverse_lazy("task_update", kwargs={"pk": 1})
        self.detail_task_view_url = reverse_lazy('task_view', kwargs={"pk": 1})
        self.delete_task1_url = reverse_lazy("task_delete", kwargs={"pk": 1})
        self.delete_task2_url = reverse_lazy("task_delete", kwargs={"pk": 2})
        self.user1 = get_user_model().objects.get(pk=1)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)


class TestNoLoginStatusesViews(SetupTestTasks):

    def test_open_tasks_page_with_no_login(self):
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 302)

    def test_open_create_task_page_with_no_login(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 302)

    def test_open_update_task_page_with_no_login(self):
        response = self.client.get(self.update_task_url)
        self.assertEqual(response.status_code, 302)

    def test_open_delete_task_page_with_no_login(self):
        response = self.client.get(self.delete_task1_url)
        self.assertEqual(response.status_code, 302)


class TestTaskList(SetupTestTasks):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def test_open_all_tasks_page(self):
        self.client.force_login(user=self.user1)
        response = self.client.get(self.tasks_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_open_all_tasks_page_without_authorization(self):
        response = self.client.get(self.tasks_url)
        self.assertRedirects(response=response,
                             expected_url=self.login_url,
                             status_code=302, target_status_code=200)

    def test_open_detail_task_view_page(self):
        self.client.force_login(user=self.user1)
        response = self.client.get(self.detail_task_view_url)
        self.assertEqual(first=response.status_code, second=200)


class TestCreateTask(SetupTestTasks):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def test_open_create_status_page_without_login(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_create_status_page_with_login(self):
        self.client.force_login(user=self.user1)
        response = self.client.get(self.create_task_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_create_task(self):
        self.client.force_login(user=self.user1)
        response = self.client.post(path=self.create_task_url,
                                    data={
                                        "name": "new task name",
                                        "description": "new task description",
                                        "status": 1,
                                        "labels": [],
                                        "author": 1,
                                        "executor": 1
                                    }
                                    )
        self.assertRedirects(response=response, expected_url=self.tasks_url)
        self.assertEqual(first=response.status_code, second=302)

        self.task3 = Task.objects.get(pk=3)
        self.assertEqual(first=self.task3.name,
                         second="new task name")


class TestUpdateTask(SetupTestTasks):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def test_open_update_tasks_page_without_login(self):
        response = self.client.get(self.update_task_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_update_tasks_page_with_login(self):
        self.client.force_login(user=self.user1)
        response = self.client.get(self.update_task_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_update_task(self):
        self.client.force_login(self.user1)
        self.task = Task.objects.get(pk=1)
        self.assertNotEqual(first=self.task.name,
                            second="new task name")

        response = self.client.post(path=self.update_task_url,
                                    data={
                                        "name": "new task name",
                                        "description": "new task description",
                                        "status": 1,
                                        "labels": [],
                                        "author": 1,
                                        "executor": 1
                                    }
                                    )
        self.assertEqual(first=response.status_code, second=302)

        self.task = Task.objects.get(pk=1)
        self.assertEqual(first=self.task.name,
                         second="new task name")


class TestDeleteTask(SetupTestTasks):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    def test_open_delete_page_without_login(self):
        response = self.client.get(path=self.delete_task1_url)
        self.assertEqual(first=response.status_code, second=302)

    def test_open_delete_page_with_login(self):
        self.client.force_login(user=self.user1)
        response = self.client.get(path=self.delete_task1_url)
        self.assertEqual(first=response.status_code, second=200)

    def test_delete_task(self):
        self.client.force_login(user=self.user1)
        response = self.client.delete(path=self.delete_task1_url)
        self.assertEqual(first=response.status_code, second=302)
        self.assertEqual(first=Task.objects.all().count(), second=1)
        with self.assertRaises(expected_exception=Task.DoesNotExist):
            Task.objects.get(pk=1)

    def test_cant_delete_task_if_user_is_not_author(self):
        self.client.force_login(user=self.user1)
        response = self.client.delete(path=self.delete_task2_url)
        self.assertEqual(first=response.status_code, second=302)
        self.assertRedirects(response=response, expected_url=self.tasks_url)
        self.assertEqual(first=Task.objects.all().count(), second=2)
