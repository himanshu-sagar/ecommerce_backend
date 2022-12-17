from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem, Product

from products.serializers import ProductSerializer, Product


class OrderAPIView(APIView):
    permission_classes = (IsAuthenticated, )  # Only authenticated user can make an order

    def post(self, request, format=None):
        data = request.data
        user = request.user  # fetch user from request

        total_amount = 0  # total price of all items in an order

        order_items_data = request.data.get('items', [])
        for item_data in order_items_data:

            # Look up the product and ensure it is in stock
            product = get_object_or_404(Product, pk=item_data['product_id'])
            if product.quantity < item_data['quantity']:
                return Response({'error': 'Not enough items in stock'}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate total price
            total_amount += product.price * item_data.get('quantity')

        order_data = {
            "customer_id": user.id,
            "shipping_address": data.get('shipping_address'),
            "total_amount": total_amount
        }

        order_serializer = OrderSerializer(data=order_data)
        if not order_serializer.is_valid():
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        order = order_serializer.save()

        # Validate and create the order items
        for item_data in order_items_data:
            # Decrease the product quantity and save the order item
            product.quantity -= item_data['quantity']
            product.save()

            item_data["order_id"] = order.order_id

            item_serializer = OrderItemSerializer(data=item_data)
            if not item_serializer.is_valid():
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            item_serializer.save()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)


class OrderHistoryAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        # Get the orders for the current user
        orders = Order.objects.filter(customer_id=request.user)

        # Serialize the orders and return them in the response
        serializer = OrderSerializer(orders, many=True)

        order_history = serializer.data

        for order in order_history:

            order_items = OrderItem.objects.filter(order_id=order["order_id"])
            order_items_serializer = OrderItemSerializer(order_items, many=True)
            order["items"] = order_items_serializer.data

            for item in order_items_serializer.data:
                product = Product.objects.filter(id=item["product_id"])
                product_serializer = ProductSerializer(product, many=True)

                item["product_details"] = product_serializer.data[0]
        return Response({"data": order_history}, status=status.HTTP_200_OK)