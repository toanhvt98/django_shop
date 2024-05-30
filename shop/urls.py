from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product/', views.product_page, name='product_page'),
    path('product/electronics', views.electronics_products_page, name='electronics_products_page'),
    path('product/shoe', views.shoe_products_page, name='shoe_products_page'),
    path('product/clothing', views.clothing_products_page, name='clothing_products_page'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),

]
