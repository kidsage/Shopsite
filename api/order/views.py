from rest_framework import viewsets
from accounts.models import User
from api.product.serializers import ProductSerializer
from order.models import Order, Cart
from product.models import Product
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



# 테스트 추가 사항 있음
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

# def my_cart(request):
#     """
#     각 유저의 장바구니 공간
#     """
#     cart_item = Cart.objects.filter(user__id=request.user.pk)
#     # 장바구니에 담긴 상품의 총 합계 가격
#     total_price = 0
#     # for loop 를 순회하여 각 상품 * 수량을 total_price 에 담는다
#     for each_total in cart_item:
#         total_price += each_total.product.price * each_total.quantity
#     if cart_item is not None:
#         context = {
#         	# 없으면 없는대로 빈 conext 를 템플릿 변수에서 사용
#             'cart_item': cart_item,
#             'total_price': total_price,
#         }
#         return render(request, 'cart/cart-list.html', context)
#     return redirect('product:my-cart')


# 세개의 함수형 뷰 통합 예정
# def minus_cart_item(request, product_pk):
#     cart_item = Cart.objects.filter(product__id=product_pk)
#     product = Product.objects.get(pk=product_pk)
#     try:
#         for item in cart_item:
#             if item.product.name == product.name:
#                 if item.quantity > 1:
#                     item.quantity -= 1
#                     item.save()
#                 return redirect('product:my-cart')
#             else:
#                 return redirect('product:my-cart')
#     except Cart.DoesNotExist:
#         raise Http404