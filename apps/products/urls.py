from django.urls import path

from .views import (
    ProductListView,
    CategoriesListView,
    SubCategoriesListView,
    ProductListAllView
)

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("categories", CategoriesListView.as_view(), name="categories"),
    path("list/<int:cat_id>", ProductListAllView.as_view(), name="all-products"),
    path("sub-categories/<int:cat_id>", SubCategoriesListView.as_view(), name="sub-categories")
]
