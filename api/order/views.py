from rest_framework import viewsets
from accounts.models import User
from api.product.serializers import ProductSerializer
from order.models import Order, Cart
from product.models import Product
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



# 장바구니 기능 테스트
# def add_cart(request, product_pk):
# 	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
#     product = Product.objects.get(pk=product_pk)

#     try:
#     	# 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
#         cart = Cart.objects.get(product__id=product.pk, user__id=request.user.pk)
#         if cart:
#             if cart.product.name == product.name:
#                 cart.quantity += 1
#                 cart.save()
#     except Cart.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = Cart(
#             user=user,
#             product=product,
#             quantity=1,
#         )
#         cart.save()
#     return redirect('product:my-cart')