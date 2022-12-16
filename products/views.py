from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class ProductCreateDeleteUpdateView(
    generics.CreateAPIView, generics.UpdateAPIView, generics.ListAPIView, generics.DestroyAPIView
):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    queryset = Product.objects.all().order_by('quantity')
