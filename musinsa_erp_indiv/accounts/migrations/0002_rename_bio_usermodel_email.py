# Generated by Django 4.2 on 2023-04-07 06:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermodel",
            old_name="bio",
            new_name="email",
        ),
    ]
