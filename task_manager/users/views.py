from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import User
from django.utils.translation import gettext_lazy as _
from .forms import UserForm

class UsersListView(ListView):
    model = User
    ordering = 'id'
    context_object_name = 'users'
    extra_context = {'title': _('Users')}
    template_name = 'users/users_list.html'

class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/user_create.html'
    extra_context = {'title': _('Registration')}
    success_url = reverse_lazy('log_in')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_update.html'
    success_message = _('User successfully changed')
    success_url = reverse_lazy('users_list')
    login_url = reverse_lazy('log_in')
    extra_context = {'title': _('Update user')}

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_message = _('User successfully deleted')
    success_url = reverse_lazy('users_list')
    extra_context = {'title': _('Delete user')}
    