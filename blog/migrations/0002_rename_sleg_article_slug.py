# Generated by Django 5.0.4 on 2024-05-24 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="sleg",
            new_name="slug",
        ),
    ]
