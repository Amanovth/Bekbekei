from rest_framework import serializers
from .models import Order, ProductInline, DeliveryAddress
from apps.products.models import Product

class ProductInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInline
        fields = ['product', 'count']
        ref_name = 'product_for_order'


class OrderSerializer(serializers.ModelSerializer):
    product_for_order = ProductInlineSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'address', 'product_for_order']

    def create(self, validated_data):
        product_data = validated_data.pop('product_for_order')
        order = Order.objects.create(**validated_data)
        total_sum = 0 
        for i in product_data:
            product_id = int(i['product'])
            product = Product.objects.get(pk=product_id)
            count = i['count']
            total_sum += product.wholesale_price * count
            ProductInline.objects.create(
                order=order,
                product=product,
                count=count
            )
        
        order.sum = total_sum
        order.save()
        return order
    
class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        exclude = ['user']