from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_("username"), max_length=65,)
    password = forms.CharField(label=_("password"), max_length=65,
                               widget=forms.PasswordInput)
