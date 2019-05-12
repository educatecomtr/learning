from .accounts import RoleView, DealerRoleView, DistributorRoleView, list_staff, create_staff, delete_staff, edit_staff
from .accounts import edit_permissions, attach_staff
from .product import ProductCreateView, ProductUpdateView, ProductListView, ProductDeleteView
from .shop import ShopListView, ShopDetailView, CartView, CartAdd, CartDelete, CartClear
from .order import OrderDetailView, OrderDeleteView, OrderAddView, OrderListView
from .payment import PaymentCreateView, PaymentListView, PaymentDistributorDetailView, PaymentDistributorListView
from .distributor import DistributorOrderApproveView, DistributorOrderDeleteView, DistributorOrderDetailView, DistributorOrderListView
from .distributor import DealerCreateView, DealerUpdateView, DealerListView, DealerDeleteView, DealerRelationView
from .distributor import DistributorPaymentApproveView, DistributorPaymentListView, DistributorPaymentDealerDetailView, DistributorPaymentDealerListView