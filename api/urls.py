from django.urls import path, include
from rest_framework import routers
from .accounts.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]