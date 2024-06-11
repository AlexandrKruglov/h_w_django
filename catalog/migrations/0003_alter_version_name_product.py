# Generated by Django 5.0.4 on 2024-06-11 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="name_product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.product",
                verbose_name="продукт",
            ),
        ),
    ]
