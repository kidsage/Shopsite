from django.urls import path, include
from rest_framework import routers
from .accounts.views import UserViewSet, AddressViewSet
from .post.views import PostViewSet, CommentViewSet
from .order.views import OrderViewSet, PaymentComplete, CartExistCheckAPI, OrderListAPI, CartListAPI
from .product.views import ProductViewSet
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'address', AddressViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'order', OrderViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order/main', TemplateView.as_view(template_name='order/order.html'),
         name='order-list'),
    path('cart/', TemplateView.as_view(template_name='order/cart.html'),
         name='cart'),
    path('cart-api/', CartListAPI.as_view(), name='cart-api'),
    path('order-api/', OrderListAPI.as_view(), name='order-api'),
    path('exist-api/', CartExistCheckAPI.as_view(), name='exist-api'),
    path('payments-complete/', PaymentComplete.as_view(),
         name='payments-complete'),
]
    
