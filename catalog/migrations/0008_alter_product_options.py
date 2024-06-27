# Generated by Django 4.2.2 on 2024-06-26 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name_product",),
                "permissions": [
                    ("can_set_published", "Сan change published status"),
                    ("can_change_product_description", "Сan change description"),
                    ("can_change_product_category", "Сan change category"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
