from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
