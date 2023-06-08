from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Label
from django.utils.translation import gettext_lazy as _
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    ordering = 'id'
    context_object_name = 'labels'
    extra_context = {'title': _('Labels')}
    login_url = reverse_lazy('log_in')
    template_name = 'labels/labels_list.html'


class LabelsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'create_form.html'
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create')
    }
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('labels_list')
    success_message = _('Label successfully created')


class LabelsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'create_form.html'
    extra_context = {
        'title': _('Update label'),
        'button_text': _('Update')}
    login_url = reverse_lazy('log_in')
    success_url = reverse_lazy('labels_list')
    success_message = _('Label successfully updated')


class LabelsDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete_label.html'
    success_message = _('Label successfully deleted')
    login_url = reverse_lazy('log_in')
    protected_message = _('It is not possible to delete a label '
                          'because it is in use')
    protected_url = reverse_lazy('labels_list')
    success_url = reverse_lazy('labels_list')
    extra_context = {'title': _('Delete label'), 'action': _('Yes, delete')}

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _('It is not possible to delete'
                           ' a label because it is in use'))
            return redirect(reverse_lazy('labels_list'))
