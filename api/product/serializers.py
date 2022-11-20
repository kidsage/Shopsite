from rest_framework import serializers
from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'created_at', 'category']

    def create(self, validated_data):

        category_data = validated_data.pop('category')
        category = Category.objects.create(
            name = category_data['name']
        )

        product = Product.objects.create(
            name = validated_data['name'],
            price = validated_data['price'],
            description = validated_data['description'],
            stock = validated_data['stock'],
            category = category
        )
        
        return product