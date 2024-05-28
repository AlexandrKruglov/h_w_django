from django.shortcuts import render, get_object_or_404
import os

from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class Product2ListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsPageVeiw(TemplateView):
    template_name = 'catalog/contacts.html'


