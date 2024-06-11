from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'prise', 'category')
    list_filter = ('category',)
    search_fields = ('name_product', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'name_product')
    list_filter = ('name_product',)

