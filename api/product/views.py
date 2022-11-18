from rest_framework import viewsets
from product.models import Product
from .serializers import ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer