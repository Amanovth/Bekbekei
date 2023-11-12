from rest_framework import serializers

from .models import (
    Product,
    Category,
    SubCategory,
)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SubCategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategoriesListSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoriesListSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "img", "sub_categories"]
