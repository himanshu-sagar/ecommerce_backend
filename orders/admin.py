from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "customer_id", "shipping_address", "order_date", "total_amount"]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order_item_id", "order_id", "product_id", "quantity"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)