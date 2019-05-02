from django.urls import path
from . import views

urlpatterns = [

    path('products/role/', views.RoleView.as_view(), name='role-list'),

]

