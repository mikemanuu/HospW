# Generated by Django 5.1.3 on 2024-11-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment", old_name="datetime", new_name="date",
        ),
    ]
