from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import (
    ProductsListView,
    UserBasketsView,
    basket_add,
    basket_remove,
    basket_remove_all,
)

app_name = "products"

urlpatterns = [
    path("", cache_page(30)(ProductsListView.as_view()), name="index"),
    path("category/<int:category_id>", ProductsListView.as_view(), name="category"),
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),
    path("baskets/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
    path("baskets/removes", basket_remove_all, name="basket_remove_all"),
    path("baskets/", UserBasketsView.as_view(), name="baskets"),
]
