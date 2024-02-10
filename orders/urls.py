from django.urls import path
from django.views.decorators.cache import cache_page

from orders.views import OrderCreateView

app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name="order_create"),
]
