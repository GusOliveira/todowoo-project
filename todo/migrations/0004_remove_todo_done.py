# Generated by Django 2.2.5 on 2020-12-01 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201129_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
    ]
