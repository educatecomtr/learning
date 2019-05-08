from .accounts import RoleView, DealerRoleView, DistributorRoleView, list_staff, create_staff, delete_staff, edit_staff
from .accounts import edit_permissions, attach_staff
from .dealer import DealerCreateView, DealerUpdateView, DealerListView, DealerDeleteView
from .product import ProductCreateView, ProductUpdateView, ProductListView, ProductDeleteView
from .shop import ShopListView, ShopDetailView, CartView, CartAdd, CartDelete, CartClear
from .order import OrderDetailView, OrderApprove, OrderDelete, OrderAdd, OrderListView

