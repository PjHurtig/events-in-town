# Generated by Django 3.2.20 on 2023-07-22 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_post_event_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='event_time',
        ),
    ]
