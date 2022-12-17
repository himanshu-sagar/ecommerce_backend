from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateDeleteUpdateView.as_view(), name='product-create-update'),
    path('list', views.ProductListView.as_view(), name='product-list'),
    path('delete/<str:pk>', views.ProductCreateDeleteUpdateView.as_view(), name='product-delete'),
    path('update_quantity/<str:pk>', views.ProductCreateDeleteUpdateView.as_view(), name='product-update-quantity')
]