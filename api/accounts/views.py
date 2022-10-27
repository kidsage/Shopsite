from ast import Mod
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from accounts.models import *
from .serializers import *

#Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profile
    permission_classes = [IsAuthenticatedOrReadOnly]