from django.shortcuts import render
import os

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
