from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    CategoriesListView,
    SubCategoriesListView,
    ProductListAllView
)

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("detail/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("categories", CategoriesListView.as_view(), name="categories"),
    path("list/<int:cat_id>", ProductListAllView.as_view(), name="all-products"),
    path("sub-categories/<int:cat_id>", SubCategoriesListView.as_view(), name="sub-categories")
]
