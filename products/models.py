from django.db import models

from users.models import User

class FlowersCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null = True, blank= True)

    class Meta:
        verbose_name = 'Вид цветка'
        verbose_name_plural = 'Категории цветов'

    def __str__(self):
        return f'{self.name}'


class CountryCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Категории стран'

    def __str__(self):
        return f'{self.name}'
    
class FlowersLength(models.Model):
    len = models.FloatField(max_length=5, unique=True)

    class Meta:
        verbose_name = 'Длинну'
        verbose_name_plural = 'Длинна цветков'

    def __str__(self):
        return f'{self.len}'


class FlowersWarehouse(models.Model):
    name = models.CharField(max_length = 256)
    category_flowers = models.ForeignKey(to = FlowersCategory, on_delete = models.PROTECT)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.PositiveBigIntegerField(default = 0)
    image = models.ImageField(upload_to = 'products_images')
    len_id = models.ForeignKey(to = FlowersLength, on_delete = models.PROTECT)
    country = models.ForeignKey(to = CountryCategory, on_delete= models.PROTECT, default= None)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Склад цветов'

    def __str__(self):
        return f'Продукт : {self.name} {self.len_id.len}см. ({self.country.name}) | Категория: {self.category_flowers.name}'
    

class FinishedProductsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null = True, blank= True)

    class Meta:
        verbose_name = 'Вид продукта'
        verbose_name_plural = 'категории конечных продуктов'

    def __str__(self):
        return f'{self.name}'

    
class FinishedProducts(models.Model):
    name = models.CharField(max_length = 256)
    category_products = models.ForeignKey(to = FinishedProductsCategory, on_delete = models.PROTECT)
    structure = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.PositiveBigIntegerField(default = 0)
    image = models.ImageField(upload_to = 'products_images')
    count = models.IntegerField()
    
    class Meta:
        verbose_name = 'Конечный продукт'
        verbose_name_plural = 'Конечные продукты'

    def __str__(self):
        return f'Продукт : {self.name} {self.structure}| Категория: {self.category_products.name}'


class ProductsToFlowers(models.Model):
    products_id = models.ForeignKey(to = FinishedProducts, on_delete = models.PROTECT)
    flowers_id = models.ForeignKey(to = FlowersWarehouse, on_delete = models.PROTECT)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Сосатав конечного продукта'
        verbose_name_plural = 'Состав конечного продукта'

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=FinishedProducts, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity
