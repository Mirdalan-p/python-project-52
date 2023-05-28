from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.


class Label(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Name'),
        unique=True,
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
