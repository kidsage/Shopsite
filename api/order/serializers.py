from rest_framework import serializers
from order.models import Order
# from ..accounts.serializers import UserSerializer
from ..product.serializers import ProductSerializer
from product.models import Product

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity']

    
    def create(self, validated_data):

        order = Order.objects.create(
            user = validated_data['user'],
            product = validated_data['product'],
            quantity = validated_data['quantity'],
        )

        # product stock update
        # 모든 product stock이 줄어드는 현상 수정 필요
        product_data = validated_data.pop('product')
        p_update = Product.objects.update(
            stock = product_data.stock - validated_data['quantity']
        )

        return order