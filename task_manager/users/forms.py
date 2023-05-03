from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
        
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']