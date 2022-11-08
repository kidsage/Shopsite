from accounts.models import *
from rest_framework import serializers
from django.contrib.auth.models import update_last_login


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


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'gender', 'date_of_birth', 'phonenumber', 'introduce', 'followings', 'followers']

    def get_followings(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data



class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, required=False)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'address', 'profile']
        extra_kwargs = {"password": {"write_only": True}}

    # def validate(self, data):
    #     user, is_created = User.objects.get_or_create(email=data["email"])
        
    #     payload   = JWT_PAYLOAD_HANDLER(user)
    #     jwt_token = JWT_ENCODE_HANDLER(payload)
        
    #     update_last_login(None, user)
        
    #     results = {
    #             'access_token' : jwt_token
    #         }

    #     return results

    # test 11/8
    # def create(self, validated_data):
    #     instance = User(**validated_data)
    #     instance.set_password(validated_data["password"])
    #     instance.save()

    #     return instance