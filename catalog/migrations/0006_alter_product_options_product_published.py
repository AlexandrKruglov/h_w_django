# Generated by Django 4.2.2 on 2024-06-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name_product",),
                "permissions": [
                    ("change_published", "can change published status"),
                    ("change_description", "can change description"),
                    ("change_category", "can change category"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="published",
            field=models.BooleanField(default=False, verbose_name="опубликован"),
        ),
    ]