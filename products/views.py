from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
 
# Create your views here.
from products.models import FlowersWarehouse, FlowersCategory, FinishedProducts, Basket, FinishedProductsCategory
from users.models import User

def index(request):
    context = {
        "title": "Flowers Store",
        "is_promotion": True,
    }
    return render(request, "products/index.html", context)


def products(request,category_id= None, page_number=1):
    products = FinishedProducts.objects.filter(category_products_id=category_id) if category_id else FinishedProducts.objects.all()
    per_page = 5
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        "title": "Flowers Store - Каталог",
        "categories" : FinishedProductsCategory.objects.all(),
        "products" : products_paginator,
    }
    return render(request, "products/products.html", context)

@login_required
def basket_add(request, product_id):
    product = FinishedProducts.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.last()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove_all(request):
    baskets = Basket.objects.filter(user=request.user)
    for basket in baskets:
        basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
