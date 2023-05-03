from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
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
