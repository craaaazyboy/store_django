from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (
    EmailVerificationVeiw,
    UserLoginView,
    UserProfileView,
    UserRegistrationView,
)

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile/<int:pk>", login_required(UserProfileView.as_view()), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "verification/<str:email>/<uuid:code>/",
        EmailVerificationVeiw.as_view(),
        name="verification",
    ),
]
