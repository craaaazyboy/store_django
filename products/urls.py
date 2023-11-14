from django.urls import path

from products.views import ProductsListView, basket_add, basket_remove, basket_remove_all

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name ='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name ='category'),
    # path('page/<int:page_number>', products, name ='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name ='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name ='basket_remove'),
    path('baskets/', basket_remove_all, name ='basket_remove_all'),
]
