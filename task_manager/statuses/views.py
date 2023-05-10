from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Status
from django.utils.translation import gettext_lazy as _

# Create your views here.

class StatusesListView(ListView):
    model = Status
    ordering = 'id'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}
    template_name = 'statuses/statuses_list.html'

class StatusCreateView(CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_create.html'
    extra_context = {'title': _('Create status')}
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully created')