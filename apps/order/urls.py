from django.urls import path
from .views import OrderView, OrdersListView, OrderCancelView, DeliveryAddressCreateView, DeliveryAddressListView, DeliveryAddressDeleteView

urlpatterns = [
    path("order", OrderView.as_view(), name="order"),
    path("list", OrdersListView.as_view(), name="order-list"),
    path("cancel/<int:order_id>/", OrderCancelView.as_view(), name="order-cancel"),
    path('address/add', DeliveryAddressCreateView.as_view(), name='address-add'),
    path('address/list/', DeliveryAddressListView.as_view(), name='address-list'),
    path('address/delete/<int:delivery_id>', DeliveryAddressDeleteView.as_view(), name='address-delete')
]