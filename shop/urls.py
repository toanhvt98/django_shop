from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('product/', RedirectView.as_view(url='/product/electronics', permanent=False), name='product'),
    path('product/electronics', views.electronics_products_page, name='electronics_products'),
    path('product/shoe', views.shoe_products_page, name='shoe_products'),
    path('product/clothing', views.clothes_products_page, name='clothes_products'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('admin/management/', RedirectView.as_view(url='/admin/management/electronics_products', permanent=False), name='admin_management'),
    path('admin/management/electronics_products', views.admin_management_electronics_products, name='admin_management_electronics_products'),
    path('admin/management/clothing_products', views.admin_management_clothing_products, name='admin_management_clothing_products'),
    path('admin/management/shoe_products', views.admin_management_shoe_products, name='admin_management_shoe_products'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
