from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [

    # shop sayfaları | dealer
    path('shop/list/', views.ShopListView.as_view(), name='list-shop'),
    path('shop/cart/detail/', views.CartView.as_view(), name='detail-cart'),
    path('shop/cart/clear/', views.CartClear.as_view(), name='clear-cart'),
    path('shop/detail/<int:pk>/', views.ShopDetailView.as_view(), name='detail-shop'),
    path('shop/cart/add/<int:pk>/', views.CartAdd.as_view(), name='add-cart'),
    path('shop/cart/delete/<int:pk>/', views.CartDelete.as_view(), name='delete-cart'),

    # sipariş sayfaları | dealer
    path('order/list/', views.OrderListView.as_view(), name='list-order'),
    path('order/create/', views.OrderAddView.as_view(), name='create-order'),
    path('order/detail/<int:pk>/', views.OrderDetailView.as_view(), name='detail-order'),
    path('order/cancel/<int:pk>/', views.OrderDeleteView.as_view(), name='cancel-order'),

    # ödeme sayfaları | dealer
    path('payment/list/', views.PaymentListView.as_view(), name='list-payment'),
    path('payment/detail/', views.PaymentDistributorListView.as_view(), name='list-detail-payment'),
    path('payment/create/', views.PaymentCreateView.as_view(), name='create-payment'),
    path('payment/distributor/<int:pk>/', views.PaymentDistributorDetailView.as_view(), name='detail-payment'),
    path('payment/cancel/<int:pk>/', views.PaymentDeleteView.as_view(), name='cancel-payment'),

    # bayi yönetimi sayfaları | distributor
    path('distributor/dealer/create/', views.DealerCreateView.as_view(), name='distributor-create-dealer'),
    path('distributor/dealer/list/', views.DealerListView.as_view(), name='distributor-list-dealer'),
    path('distributor/dealer/attach/', views.DealerRelationView.as_view(), name='distributor-attach-dealer'),
    path('distributor/dealer/edit/<int:pk>/', views.DealerUpdateView.as_view(), name='distributor-edit-dealer'),
    path('distributor/dealer/delete/<int:pk>/', views.DealerDeleteView.as_view(), name='distributor-delete-dealer'),

    # sipariş sayfaları | distributor
    path('distributor/order/list/', views.DistributorOrderListView.as_view(), name='distributor-list-order'),
    path('distributor/order/detail/<int:pk>/', views.DistributorOrderDetailView.as_view(), name='distributor-detail-order'),
    path('distributor/order/approve/<int:pk>/', views.DistributorOrderApproveView.as_view(), name='distributor-approve-order'),
    path('distributor/order/cancel/<int:pk>/', views.DistributorOrderDeleteView.as_view(), name='distributor-cancel-order'),

    # ödeme sayfaları | distributor
    path('distributor/payment/list/', views.DistributorPaymentListView.as_view(), name='distributor-list-payment'),
    path('distributor/payment/detail/', views.DistributorPaymentDealerListView.as_view(), name='distributor-list-detail-payment'),
    path('distributor/payment/approve/<int:pk>/', views.DistributorPaymentApproveView.as_view(), name='distributor-approve-payment'),
    path('distributor/payment/delete/<int:pk>/', views.DistributorPaymentDeleteView.as_view(), name='distributor-cancel-payment'),
    path('distributor/payment/dealer/<int:pk>/', views.DistributorPaymentDealerDetailView.as_view(), name='distributor-detail-payment'),

    # ürün yönetimi sayfaları | distributor
    path('distributor/product/list/', views.ProductListView.as_view(), name='distributor-list-product'),
    path('distributor/product/create/', views.ProductCreateView.as_view(), name='distributor-create-product'),
    path('distributor/product/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='distributor-edit-product'),
    path('distributor/product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='distributor-delete-product'),



]