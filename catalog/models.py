from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="категория")
    description = models.TextField(verbose_name="описание", **NULLABLE)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name_category",)


class Product(models.Model):
    name_product = models.CharField(max_length=50, verbose_name="продукт")
    description = models.TextField(default="-", verbose_name="описание")
    image = models.ImageField(
        upload_to="image/", verbose_name="изображение", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        **NULLABLE,
        related_name="products",
    )
    prise = models.FloatField(verbose_name="цена")
    created_at = models.DateField(verbose_name="дата создания")
    updated_at = models.DateField(verbose_name="дата последнего изменения")
    owner = models.ForeignKey(User, verbose_name="создатель", **NULLABLE, on_delete=models.SET_NULL)
    published = models.BooleanField(default=False, verbose_name="опубликован")

    def __str__(self):
        return f"{self.name_product}, {self.prise}, {self.created_at}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name_product",)
        permissions = [
            ("can_set_published", "Сan change published status"),
            ("can_change_product_description", "Сan change description"),
            ("can_change_product_category", "Сan change category")
        ]


class Version(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя версии")
    number = models.IntegerField(verbose_name="номер версии")
    name_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        **NULLABLE,
    )
    activ = models.BooleanField(default=True, verbose_name="активная")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
