from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductCreateDeleteUpdateView.as_view(), name='product-create-update'),
    path('product/list', views.ProductListView.as_view(), name='product-list'),
    path('product/delete/<str:pk>', views.ProductCreateDeleteUpdateView.as_view(), name='product-delete'),
    path(
        'product/update_quantity/<str:pk>',
        views.ProductCreateDeleteUpdateView.as_view(),
        name='product-update-quantity'
    )
]