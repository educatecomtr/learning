from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [

    path('dealer/create/', views.DealerCreateView.as_view(), name='create-dealer'),
    path('dealer/edit/<int:pk>/', views.DealerUpdateView.as_view(), name='edit-dealer'),
    path('dealer/delete/<int:pk>/', views.DealerDeleteView.as_view(), name='delete-dealer'),
    path('dealer/list/', views.DealerListView.as_view(), name='list-dealer'),

    path('product/create/', views.ProductCreateView.as_view(), name='create-product'),
    path('product/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit-product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete-product'),
    path('product/list/', views.ProductListView.as_view(), name='list-product'),

    path('shop/list/', views.ShopListView.as_view(), name='list-shop'),

]

