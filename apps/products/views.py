from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .filters import ProductFilter
from .models import (
    Product,
    Category
)
from .serializer import (
    ProductListSerializer,
    CategoriesListSerializer
)


class ProductListView(ListAPIView):
    queryset = Product.objects.select_related("cat", "sub_cat")
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "cat__name", "sub_cat__name", "code"]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", "-id")

        return queryset.order_by(ordering)


class CategoriesListView(ListAPIView):
    queryset = Category.objects.prefetch_related("sub_categories")
    serializer_class = CategoriesListSerializer
