from django.db import models
from products.models import Product
from authentication.models import User


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, auto_created=True)
    customer_id = models.ForeignKey(to=User, on_delete=models.CASCADE, to_field="id")
    shipping_address = models.CharField(max_length=500)
    order_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    total_amount = models.FloatField()


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True, auto_created=True)
    order_id = models.ForeignKey(to=Order, on_delete=models.CASCADE, to_field="order_id")
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE, to_field="id")
    quantity = models.PositiveIntegerField()
