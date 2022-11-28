from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
        # 일단 name으로 맞춰주긴 했는데, 뭔가 2번에 걸쳐 돌아가는 느낌이기는 하다.
        product_data = validated_data.pop('product')
        if product_data.stock != 0:
            p_update = Product.objects.filter(name=product_data.name).update(
                stock = product_data.stock - validated_data['quantity']
            )
        else:
            raise ValidationError('남은 수량이 없습니다.')

        return order