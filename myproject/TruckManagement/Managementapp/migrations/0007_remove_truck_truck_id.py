# Generated by Django 4.0.7 on 2022-09-29 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0006_rename_truck_assigntruck_vehicle_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="truck",
            name="truck_id",
        ),
    ]
