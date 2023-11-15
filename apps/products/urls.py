from django.urls import path

from .views import (
    ProductListView,
    CategoriesListView,
    SubCategoriesListView
)

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("categories", CategoriesListView.as_view(), name="categories"),
    path("sub-categories/<int:cat_id>", SubCategoriesListView.as_view(), name="sub-categories")
]
