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

        # p_update = Product.objects.update(
        #     pk = self.product.pk,
        #     stock = self.product['stock'] - validated_data['quantity']
        # )

        return order