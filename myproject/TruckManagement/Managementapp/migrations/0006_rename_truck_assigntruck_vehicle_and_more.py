# Generated by Django 4.0.7 on 2022-09-29 08:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Managementapp", "0005_remove_company_detail_emp_record_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assigntruck",
            old_name="truck",
            new_name="vehicle",
        ),
        migrations.AddField(
            model_name="assigntruck",
            name="issue_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="assigntruck",
            name="return_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="assigntruck",
            name="driver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Managementapp.company_detail",
            ),
        ),
    ]
