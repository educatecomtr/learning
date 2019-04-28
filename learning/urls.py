from django.urls import path, re_path
from . import views

urlpatterns = [
    path('example/', views.examples),

    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('product/archive/<int:year>/<int:month>/', views.product_archive, name='product-archive'),
    path('product/add/', views.product_form, name='add-product'),
    path('product/edit/<int:pk>/', views.product_edit_form, name='edit-product'),

    path('contact/', views.contact_form, name='contact'),
]