from django.contrib import admin

# Register your models here.

from products.models import FlowersWarehouse, FlowersCategory, FlowersLength, CountryCategory, FinishedProducts, FinishedProductsCategory, ProductsToFlowers, Basket

admin.site.register(FlowersWarehouse)
admin.site.register(FlowersCategory)
admin.site.register(FlowersLength)
admin.site.register(CountryCategory)
admin.site.register(FinishedProductsCategory)
admin.site.register(ProductsToFlowers)

@admin.register(FinishedProducts)
class FinishedProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category_products')
    fields = ('name','category_products','structure',('price','quantity'),'image','count')
    search_fields = ('name',)
    ordering =('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product','created_timestamp')
    extra = 0
