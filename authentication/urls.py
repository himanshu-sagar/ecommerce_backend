from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('signup/', views.SignupAPIView.as_view(), name = "signup")
]