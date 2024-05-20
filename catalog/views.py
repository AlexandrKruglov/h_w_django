from django.shortcuts import render, get_object_or_404
import os

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open(os.path.join("cont.txt"), 'a', encoding="utf-8") as f:
            f.write(f"nane: {name}, phone: {phone}, message: {message}")
    return render(request, 'contacts.html')


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detal(request, pk):
    one_product = Product.objects.get(pk=pk)
    context = {'one_product': one_product}
    return render(request, 'product_detal', context)
