from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name=_('Name')
    )
    description = models.TextField(
        max_length=10000,
        blank=True,
        verbose_name=_('Description')
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='executor',
        null=True,
        blank=True,
        verbose_name=_('Executor')
    )
    created_at = models.DateTimeField(default=timezone.now)
    labels = models.ManyToManyField(
        Label,
        through='TaskLabelRelation',
        through_fields=('task', 'label'),
        blank=True,
        related_name='labels',
        verbose_name=_('Labels')
    )

    def __str__(self):
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
