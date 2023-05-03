from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': _('Task manager')}

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('index_page')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
    
def log_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('index_page')