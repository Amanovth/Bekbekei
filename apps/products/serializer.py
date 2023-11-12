from rest_framework import serializers

from .models import (
    Product,
    Category,
    SubCategory,
)


class ProductListSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_img(self, obj):
        return f"http://89.223.126.144:8000{obj.img.url}"


class SubCategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategoriesListSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoriesListSerializer(many=True)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "img", "sub_categories"]

    def get_img(self, obj):
        return f"http://89.223.126.144:8000{obj.img.url}"
