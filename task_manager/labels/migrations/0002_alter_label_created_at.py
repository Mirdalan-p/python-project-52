# Generated by Django 4.2 on 2023-05-28 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
