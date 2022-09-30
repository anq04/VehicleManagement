# Generated by Django 4.0.7 on 2022-09-29 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0019_alter_driver_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="user",
        ),
        migrations.AlterField(
            model_name="driver",
            name="username",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="driver",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]