import json

from django.core.management import BaseCommand
from catalog.models import Product, Category
import os.path


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(os.path.join("data.json")) as file:
            temp = json.load(file)
            list_category = []
            for item in temp:
                if item["model"] == "catalog.category":
                    list_category.append(item)
        return list_category

    @staticmethod
    def json_read_products():
        with open(os.path.join("data.json")) as file:
            temp = json.load(file)
            list_product = []
            for item in temp:
                if item["model"] == "catalog.product":
                    list_product.append(item)
        return list_product

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_for_create = []
        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(Category(id=category['pk'],
                                                name_category=category['fields']['name_category'],
                                                description=category['fields']['description']))
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(name_product=product['fields']['name_product'],
                                                description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product["fields"]["category"]),
                                              prise=product['fields']['prise'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))
        Product.objects.bulk_create(product_for_create)
