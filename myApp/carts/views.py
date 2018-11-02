from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, "carts/home.html", {})


def cart_update(request):
    obj = Product.objects.get(id=1)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(obj)

    return redirect("cart:home")
