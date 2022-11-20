from django.urls import path, include
from rest_framework import routers
from .accounts.views import UserViewSet
from .post.views import PostViewSet, CommentViewSet
from .order.views import OrderViewSet
from .product.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'order', OrderViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]