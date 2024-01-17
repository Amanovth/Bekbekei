from django.urls import path
from .views import OrderView, OrdersListView, OrdersDetailView, OrderCancelView, DeliveryAddressCreateView, DeliveryAddressListView, DeliveryAddressDeleteView, OrderTableView, OrderTableDetailView

urlpatterns = [
    path("order", OrderView.as_view(), name="order"),
    path("list", OrdersListView.as_view(), name="order-list"),
    path("<int:pk>", OrdersDetailView.as_view(), name='order-detail'),
    path("cancel/<int:order_id>/", OrderCancelView.as_view(), name="order-cancel"),
    path('address/add', DeliveryAddressCreateView.as_view(), name='address-add'),
    path('address/list/', DeliveryAddressListView.as_view(), name='address-list'),
    path('address/delete/<int:delivery_id>', DeliveryAddressDeleteView.as_view(), name='address-delete'),
    path('table/list', OrderTableView.as_view(), name='order-table'),
    path('table/<int:pk>/', OrderTableDetailView.as_view(), name='order-detail'),
]