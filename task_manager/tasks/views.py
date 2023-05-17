from django.shortcuts import render, redirect
from django.views.generic import (DetailView, 
                                  ListView, 
                                  CreateView, 
                                  DeleteView, 
                                  UpdateView
                                 )
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .mixins import DeleteTaskPermission
from task_manager.users.models import User
from task_manager.mixins import AppLoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
# Create your views here.

class TaskListView(AppLoginRequiredMixin, ListView):
    model = Task
    ordering = 'id'
    context_object_name = 'tasks'
    login_url = reverse_lazy('log_in')
    extra_context = {'title': _('Tasks')}
    template_name = 'tasks/tasks_list.html'
    
class TaskCreateView(AppLoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor']
    template_name = 'tasks/create_task.html'
    extra_context = {'title': _('Create task')}
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)



class TaskUpdateView(AppLoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor']
    template_name = 'tasks/task_update.html'
    extra_context = {'title': _('Update task')}
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task successfully updated')

class TaskDeleteView(DeleteTaskPermission, AppLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_message = _('Status successfully deleted')
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'title': _('Delete status')}

class TaskView(AppLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task.html"
    context_object_name = "task"
    extra_context = {'title': _('Task view')}