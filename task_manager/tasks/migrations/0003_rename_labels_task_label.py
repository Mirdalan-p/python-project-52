# Generated by Django 4.2 on 2023-05-28 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='labels',
            new_name='label',
        ),
    ]
