# Generated by Django 4.0.7 on 2022-09-30 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0024_alter_assigntruck_driver"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assigntruck",
            name="driver",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="Managementapp.driver"
            ),
        ),
    ]
