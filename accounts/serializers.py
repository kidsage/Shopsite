from importlib.metadata import requires
from rest_framework import serializers

from .models import *

#
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['address', 'zip_code', 'tag', 'receiver_name']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'gender', 'date_of_birth', 'phonenumber', 'introduce']


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = User
        # default 값이 있는 필드는 data들어올 때 key, value가 없어도 validate 통과 //
        fields = ['email', 'password', 'password2', 'is_seller', 'profile', 'address']

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error" : "password do not match"})
        
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue

            setattr(instance, key, value)
        instance.save()

        return instance

    def get_profile(self, obj):
        queryset = Profile.objects.all(profile_id=obj.id)
        serializer = ProfileSerializer(queryset, many=True)

        return serializer.data

    def get_address(self, obj):
        queryset = Address.objects.all()
        serializer = AddressSerializer(address_id=obj.id)

        return serializer.data