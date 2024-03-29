# Generated by Django 4.2.6 on 2023-11-19 11:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_basket"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="countrycategory",
            options={
                "verbose_name": "Страну",
                "verbose_name_plural": "Категории стран",
            },
        ),
        migrations.AlterModelOptions(
            name="finishedproducts",
            options={
                "verbose_name": "Конечный продукт",
                "verbose_name_plural": "Конечные продукты",
            },
        ),
        migrations.AlterModelOptions(
            name="finishedproductscategory",
            options={
                "verbose_name": "Вид продукта",
                "verbose_name_plural": "категории конечных продуктов",
            },
        ),
        migrations.AlterModelOptions(
            name="flowerscategory",
            options={
                "verbose_name": "Вид цветка",
                "verbose_name_plural": "Категории цветов",
            },
        ),
        migrations.AlterModelOptions(
            name="flowerslength",
            options={"verbose_name": "Длинну", "verbose_name_plural": "Длинна цветков"},
        ),
        migrations.AlterModelOptions(
            name="flowerswarehouse",
            options={"verbose_name": "Цветок", "verbose_name_plural": "Склад цветов"},
        ),
        migrations.AlterModelOptions(
            name="productstoflowers",
            options={
                "verbose_name": "Сосатав конечного продукта",
                "verbose_name_plural": "Состав конечного продукта",
            },
        ),
    ]
