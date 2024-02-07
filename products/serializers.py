from rest_framework import serializers

from products.models import FinishedProducts
from users.models import User

class FinishedProductsSerializer(serializers.ModelSerializer):
    category_products = serializers.SlugRelatedField(slug_field='name', read_only = True)
    class Meta:
        model = FinishedProducts
        fields = ('id','name','category_products','structure','price','quantity','image','count')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')
