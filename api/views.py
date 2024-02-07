from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes

from products.models import FinishedProducts
from products.serializers import FinishedProductsSerializer, UsersSerializer
from users.models import User
from products.serializers import UsersSerializer


class FinishedProductsListAPIView(ListAPIView):
    queryset = FinishedProducts.objects.all()
    serializer_class = FinishedProductsSerializer

@permission_classes([IsAuthenticated])
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
