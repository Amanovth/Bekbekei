from rest_framework import serializers

from .models import (
    Product,
    Category,
    SubCategory,
)


class ProductSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_img(self, obj):
        return f"https://bekbekei.store{obj.img.url}"


class SubCategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategoriesListSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "img"]

    def get_img(self, obj):
        return f"https://bekbekei.store{obj.img.url}"
