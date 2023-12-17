from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .filters import ProductFilter
from .models import (
    Product,
    Category,
    SubCategory
)
from .serializer import (
    ProductSerializer,
    CategoriesListSerializer,
    SubCategoriesListSerializer
)


class ProductListView(ListAPIView):
    queryset = Product.objects.select_related("cat", "sub_cat")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "cat__name", "sub_cat__name", "code"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=True)
        ordering = self.request.query_params.get("ordering", "-id")
        if ordering:
            return queryset.order_by(ordering)
        return queryset


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductSerializer


class CategoriesListView(ListAPIView):
    queryset = Category.objects.prefetch_related("sub_categories")
    serializer_class = CategoriesListSerializer


class SubCategoriesListView(ListAPIView):
    serializer_class = SubCategoriesListSerializer

    def get_queryset(self):
        return SubCategory.objects.filter(cat_id=self.kwargs["cat_id"])


class ProductListAllView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(cat_id=self.kwargs["cat_id"], status=True)
