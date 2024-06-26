# Generated by Django 5.0.4 on 2024-05-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_sleg_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="caunt_views",
            field=models.IntegerField(default=0, verbose_name="просмотры"),
        ),
        migrations.AlterField(
            model_name="article",
            name="name",
            field=models.CharField(max_length=100, verbose_name="заголовок"),
        ),
        migrations.AlterField(
            model_name="article",
            name="publication",
            field=models.BooleanField(default=True, verbose_name="опубликовано"),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.CharField(max_length=100, verbose_name="slug"),
        ),
    ]
