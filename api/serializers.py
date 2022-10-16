from rest_framework import serializers
from accounts.models import *


#
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['address', 'zip_code', 'tag', 'receiver_name']

    def create(self, validated_data):
        instance = Address(**validated_data)
        instance.user = self.context["request"].user
        instance.save()

        return instance
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'gender', 'date_of_birth', 'phonenumber', 'introduce']


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, required=False)
    profile = ProfileSerializer(required=False)
    # profile = serializers.SerializerMethodField()
    # address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'password', 'address', 'profile']

    def create(self, validated_data):
        instance = User(**validated_data)
        instance.set_password(validated_data["password"])
        instance.save()

        return instance

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue

            setattr(instance, key, value)
        instance.save()

        return instance

    # def get_profile(self, obj):
    #     queryset = Profile.objects.all(profile_id=obj.id)
    #     serializer = ProfileSerializer(queryset, many=True)

    #     return serializer.data

    # def get_address(self, obj):
    #     queryset = Address.objects.all()
    #     serializer = AddressSerializer(address_id=obj.id)

    #     return serializer.data