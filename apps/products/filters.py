import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    pricefrom = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    priceto = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = [
            "cat",
            "sub_cat",
            "pricefrom",
            "priceto"
        ]
