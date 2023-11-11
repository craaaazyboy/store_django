from django.shortcuts import render

# Create your views here.
from products.models import FlowersWarehouse, FlowersCategory, FinishedProducts

def index(request):
    context = {
        "title": "Flowers Store",
        "is_promotion": True,
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "Flowers Store - Каталог",
        "products": FlowersWarehouse.objects.all(),
        "categories" : FlowersCategory.objects.all(),
    }
    return render(request, "products/products.html", context)
