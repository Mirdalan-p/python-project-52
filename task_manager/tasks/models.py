from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.statuses.models import Status

# Create your models here.

class Task(models.Model):
    name = models.CharField(
        max_length=30, 
        verbose_name=_('Name')
    )
    description = models.CharField(
        max_length=150, 
        verbose_name=_('Description')
    )
    status = models.ForeignKey(
        Status, 
        on_delete=models.PROTECT, 
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='executor_of_task',
        null=True,
        blank=True,
        verbose_name=_('Executor')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name