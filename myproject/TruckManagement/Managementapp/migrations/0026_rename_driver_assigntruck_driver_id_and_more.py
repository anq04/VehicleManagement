# Generated by Django 4.0.7 on 2022-09-30 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0025_alter_assigntruck_driver"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assigntruck",
            old_name="driver",
            new_name="driver_id",
        ),
        migrations.RenameField(
            model_name="assigntruck",
            old_name="vehicle",
            new_name="vehicle_id",
        ),
    ]
