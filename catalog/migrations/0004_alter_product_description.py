# Generated by Django 5.0.4 on 2024-06-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_version_name_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(default="-", verbose_name="описание"),
        ),
    ]
