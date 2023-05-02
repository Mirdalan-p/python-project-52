from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': _('Task manager')}