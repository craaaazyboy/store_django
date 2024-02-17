from django.urls import path
from django.views.decorators.cache import cache_page

from orders.views import OrderCreateView, SuccessTemplateView, CanceledTemplateView, OrderListView, OrderDetailView

app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreateView.as_view(), name="order_create"),
    path("order_success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order_canceled/", CanceledTemplateView.as_view(), name="order_canceled"),
    path("", OrderListView.as_view(), name="orders_list"),
    path("order/<int:pk>", OrderDetailView.as_view(), name="order"),
]
