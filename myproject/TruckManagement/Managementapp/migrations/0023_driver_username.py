# Generated by Django 4.0.7 on 2022-09-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0022_alter_driver_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="username",
            field=models.CharField(max_length=20, null=True),
        ),
    ]