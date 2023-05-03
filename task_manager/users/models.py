from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length=150, 
        unique=True, 
        verbose_name=_('Username')
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('First name')
    )
    last_name = models.CharField(
        max_length=100, 
        verbose_name=_('Last name')
        )
    password = models.CharField(
        max_length=100,
        verbose_name=_('Password'))

    def __str__(self):
        return self.username