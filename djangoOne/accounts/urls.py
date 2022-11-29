from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create-order/', views.createOrder, name='createOrder'),
    path('update-order/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    
]
