from rest_framework import serializers
from .models import Order, ProductInline, DeliveryAddress, OrderTable, OrderTableInfo
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
    
    def validate(self, attrs):
        address = attrs.get("address")
        if not address:
            raise serializers.ValidationError({"address": "Добавьте адрес прежде чем заказать"})
        
        return super().validate(attrs)
    
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
                count=count,
                price_for=product.price_for
            )
        
        order.sum = total_sum
        order.save()
        return order
    

class ProductInlineGETSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = ProductInline
        fields = ['product', 'count', 'price', 'price_for']
    
    def get_price(self, obj):
        try:
            product = Product.objects.get(title=obj.product)
            return product.wholesale_price
        except Product.DoesNotExist:
            return None
        


class OrderListSrializer(serializers.ModelSerializer):
    product_for_order = ProductInlineGETSerializer(many=True)
    address = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'address', 'sum', 'datetime', 'key', 'product_for_order']

    def get_address(self, obj):
        if obj.address:
            return obj.address.address
        return None
    
    def get_key(self, obj):
        return True
    
    
    
class DeliveryAddressSerializer(serializers.ModelSerializer):
    active = serializers.SerializerMethodField()

    class Meta:
        model = DeliveryAddress
        fields = ['id', 'address', 'status', 'active']
    
    def get_active(self, obj):
        return False



# class OrderTableInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderTableInfo
#         fields = ['id', 'user', 'user_info', 'count']

# class OrderTableSerializer(serializers.ModelSerializer):
#     order_info = OrderTableInfoSerializer(many=True)

#     class Meta:
#         model = OrderTable
#         fields = ['id', 'product', 'order_info']