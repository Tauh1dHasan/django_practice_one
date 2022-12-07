from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='userPage'),
    path('account/', views.accountSettings, name='account'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create-order/<str:pk>/', views.createOrder, name='createOrder'),
    path('update-order/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    
]
