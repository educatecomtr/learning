from django.urls import path, re_path
from . import views

urlpatterns = [
    path('example/', views.examples),
    path('product/', views.products, name='product-list'),
    path('product/detail/<int:pk>/', views.product, name='product-detail'),
    path('product/archive/<int:year>/<int:month>/', views.product_archive, name='product-archive'),
]