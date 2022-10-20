from accounts.models import *
from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

#
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER  = api_settings.JWT_ENCODE_HANDLER

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

    def validate(self, data):
        user, is_created = User.objects.get_or_create(email=data["email"])
        
        # if is_created:
        #     subcategory_ids = Subcategory.objects.filter(category_id=1).values_list('id', flat=True)
        #     Filter.objects.bulk_create(
        #         [Filter(user_id = user.id, subcategory_id = id) for id in subcategory_ids]
        #     )
        
        payload   = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        
        update_last_login(None, user)
        
        results = {
                'access_token' : jwt_token
            }

        return results

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