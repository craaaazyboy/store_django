from django.contrib import admin

# Register your models here.

from products.models import FlowersWarehouse, FlowersCategory, FlowersLength, CountryCategory, FinishedProducts, FinishedProductsCategory, ProductsToFlowers

admin.site.register(FlowersWarehouse)
admin.site.register(FlowersCategory)
admin.site.register(FlowersLength)
admin.site.register(CountryCategory)
admin.site.register(FinishedProducts)
admin.site.register(FinishedProductsCategory)
admin.site.register(ProductsToFlowers)
