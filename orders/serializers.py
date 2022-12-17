from rest_framework.serializers import ModelSerializer, ListSerializer, PrimaryKeyRelatedField
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(ModelSerializer):
    # order_id = PrimaryKeyRelatedField(queryset=Order.objects.all())
    # product_id = PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
