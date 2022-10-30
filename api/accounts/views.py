from ast import Mod
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import *
from .serializers import *

#Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        headers = self.get_success_headers(serializer.data)

        res = Response(
            {
                "user": serializer.data,
                "message": "register successs",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token,
                },
            },
            status=status.HTTP_201_CREATED,
        )
        
        res.set_cookie("access", access_token, httponly=False)
        res.set_cookie("refresh", refresh_token, httponly=False)

        try:
            return Response(res, headers=headers)
        except:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profile
    permission_classes = [IsAuthenticated]