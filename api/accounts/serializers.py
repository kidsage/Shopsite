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
    # followings = serializers.SerializerMethodField()
    # followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'gender', 'date_of_birth', 'phonenumber', 'introduce'] #, 'followings', 'followers']

    # follow test
    # def get_followings(self, obj):
    #     return FollowingSerializer(obj.following.all(), many=True).data

    # def get_followers(self, obj):
    #     return FollowersSerializer(obj.followers.all(), many=True).data



class UserSerializer(serializers.ModelSerializer):
    
    # address를 해결해봅시다.
    address = AddressSerializer(many=True, required=False) #, queryset=Address.objects.all())
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'profile','address']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # create user 
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
        )
        # create profile
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user = user,
            nickname = profile_data['nickname'],
            image = profile_data['image'],
            gender = profile_data['gender'],
            date_of_birth = profile_data['date_of_birth'],
            phonenumber = profile_data['phonenumber'],
            introduce = profile_data['introduce'],
        )

        return user