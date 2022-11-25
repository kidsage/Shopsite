from rest_framework import viewsets
from api.product.serializers import ProductSerializer
from order.models import Order
from product.models import Product
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer