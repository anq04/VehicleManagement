# Generated by Django 4.0.7 on 2022-09-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0015_driver_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="username",
        ),
    ]