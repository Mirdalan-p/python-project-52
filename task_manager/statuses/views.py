from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Status
from django.utils.translation import gettext_lazy as _


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    ordering = 'id'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}
    login_url = reverse_lazy('log_in')
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'create_form.html'
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create')}
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully created')


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'create_form.html'
    extra_context = {
        'title': _('Update status'),
        'button_text': _('Update')}
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status successfully updated')


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    success_message = _('Status successfully deleted')
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('statuses_list')
    extra_context = {'title': _('Delete status'), 'action': _('Yes, delete')}
