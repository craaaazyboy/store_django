from django.db import models

# Create your models here. 

class FlowersCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null = True, blank= True)

    def __str__(self):
        return f'{self.name}'


class CountryCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class FlowersLength(models.Model):
    len = models.FloatField(max_length=5, unique=True)

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

    def __str__(self):
        return f'Продукт : {self.name} {self.len_id.len}см. ({self.country.name}) | Категория: {self.category_flowers.name}'
    

class FinishedProductsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null = True, blank= True)

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

    def __str__(self):
        return f'Продукт : {self.name} {self.structure}| Категория: {self.category_products.name}'


class ProductsToFlowers(models.Model):
    products_id = models.ForeignKey(to = FinishedProducts, on_delete = models.PROTECT)
    flowers_id = models.ForeignKey(to = FlowersWarehouse, on_delete = models.PROTECT)
    count = models.IntegerField()
