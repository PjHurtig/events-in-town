# Generated by Django 3.2.20 on 2023-07-22 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20230722_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]