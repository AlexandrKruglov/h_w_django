from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
import os

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.form import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class Product2ListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')


class ContactsPageVeiw(TemplateView):
    template_name = 'catalog/contacts.html'


