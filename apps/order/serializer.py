from rest_framework import serializers
from .models import Order, ProductInline

class ProductInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInline
        fields = ['product', 'count']
        ref_name = 'product_for_order'


class OrderSerializer(serializers.ModelSerializer):
    product_for_order = ProductInlineSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'number', 'product_for_order']

    def create(self, validated_data):
        product_data = validated_data.pop('product_for_order')
        order = Order.objects.create(**validated_data)
        for i in product_data:
            ProductInline.objects.create(
                order=order,
                product=i['product'],
                count=i['count']
            )
        return order