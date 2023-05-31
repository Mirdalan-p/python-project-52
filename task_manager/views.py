from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': _('Task manager')}


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        title = _('Log in')
        return render(request, 'login.html', {'form': form, 'title': title})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, _('You are logged in'))
                return redirect('index_page')

        # form is not valid or user is not authenticated
        messages.error(
            request,
            _('Please, use correct username and password.')
            )
        return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    messages.success(request, _('U are logged out'))
    return redirect('index_page')

def index(request):
    a = None
    a.hello() # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")
