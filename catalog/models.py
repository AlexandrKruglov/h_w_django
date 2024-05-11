from django.db import models

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
    description = models.TextField(verbose_name="описание", **NULLABLE)
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

    def __str__(self):
        return f"{self.name_product}, {self.prise}, {self.created_at}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name_product",)

