from http import HTTPStatus
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse

from django.utils.timezone import now

from users.models import User, EmailVerification


class UserRegistrationViewTestCase(TestCase):
    fixtures = ["socialapp.json"]

    def setUp(self):
        self.data = {
            "first_name": "илья",
            "last_name": "кондратьев",
            "username": "crazy_boy",
            "email": "i.kondratev2002@mail.ru",
            "password1": "01041973zA",
            "password2": "01041973zA",
        }
        self.path = reverse("users:registration")

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Регистрация")
        self.assertTemplateUsed(response, "users/registration.html")

    def test_user_registration_post_success(self):
        username = self.data["username"]
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("users:login"))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date(),
        )

    def test_user_registration_post_error(self):
        user = User.objects.create(username=self.data["username"])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Пользователь с таким именем уже существует.", html=True
        )
