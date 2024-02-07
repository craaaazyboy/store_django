from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import FinishedProducts, FinishedProductsCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse("index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Flowers store - Главная")
        self.assertTemplateUsed(response, "products/index.html")


class ProductsListViewTestCase(TestCase):

    def test_list(self):
        fixtures = ["FinishedProducts.json", "FinishedProductsCategory"]

        path = reverse("products:index")
        response = self.client.get(path)

        produxts = FinishedProducts.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Flowers Store - Каталог")
        self.assertTemplateUsed(response, "products/products.html")
        # self.assertEqual(list(response.context_data['object_list']), list(FinishedProducts))

    # def test_list_with_category(self):
    #     category = FinishedProductsCategory.objects.first()
    #     print(category)
    #     path = reverse("products:category", kwargs={"category_id": category.id})
    #     response = self.client.get(path)

    #     products = FinishedProducts.objects.all()
    #     print(products)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertEqual(response.context_data["title"], "Flowers Store - Каталог")
    #     self.assertTemplateUsed(response, "products/products.html")
    #     self.assertEqual(
    #         list(response.context_data["object_list"]),
    #         list(products.filter(category_id=category.id)),
    #     )
