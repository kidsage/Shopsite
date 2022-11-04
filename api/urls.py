from django.urls import path, include
from rest_framework import routers
from .accounts.views import UserViewSet
from .post.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]