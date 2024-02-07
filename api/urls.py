from django.urls import include,path, re_path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import FinishedProductsListAPIView , UserModelViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r'users', UserModelViewSet)

urlpatterns = [
    path('product-list/', FinishedProductsListAPIView.as_view(), name = 'prosuct_list'),
    path('',include(router.urls)),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
