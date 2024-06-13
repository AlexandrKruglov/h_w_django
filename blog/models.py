from django.db import models

NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    name = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.CharField(max_length=100, verbose_name="slug")
    description = models.TextField(verbose_name="содержимое")
    image = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )
    created_at = models.DateField(verbose_name="дата создания")
    publication = models.BooleanField(default=True, verbose_name="опубликовано")
    caunt_views = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ("name",)
