from django.urls import path

from .views import (
    ProductListView,
    CategoriesListView
)

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("categories", CategoriesListView.as_view(), name="categories")
]
