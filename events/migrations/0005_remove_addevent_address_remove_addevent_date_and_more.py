# Generated by Django 4.0.4 on 2022-06-11 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_addevent_delete_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addevent',
            name='address',
        ),
        migrations.RemoveField(
            model_name='addevent',
            name='date',
        ),
        migrations.RemoveField(
            model_name='addevent',
            name='phone',
        ),
    ]
