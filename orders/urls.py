from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderAPIView.as_view(), name='create-order'),
    path('history/', views.OrderHistoryAPIView.as_view(), name='order-history'),
]