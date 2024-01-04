from django.urls import path
from .views import OrderView, OrdersListView, OrderCancelView

urlpatterns = [
    path("order", OrderView.as_view(), name="order"),
    path("list", OrdersListView.as_view(), name="order-list"),
    path("cancel/<int:order_id>/", OrderCancelView.as_view(), name="order-cancel"),
]