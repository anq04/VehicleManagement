# Generated by Django 4.0.7 on 2022-09-29 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "Managementapp",
            "0010_company_detail_rental_code_driver_rental_code_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="rental_code",
        ),
    ]
