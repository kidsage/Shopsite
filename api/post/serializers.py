from rest_framework import serializers
from post.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'like']

    # like 테스트
    # def create(self, validated_data):

    #     post = Post.objects.create(
    #         title = validated_data['title'],
    #         content = validated_data['content'],
    #         tags = validated_data['tags'],
    #         lite = validated_data['like']
    #     )

    #     return post


# post comment test 진행 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'