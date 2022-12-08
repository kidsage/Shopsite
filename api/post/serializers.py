from rest_framework import serializers
from post.models import *


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'like']

    # like, tag 테스트
    def create(self, validated_data):
        
        tags_data = validated_data.pop('tags')

        post = Post.objects.create(
            title = validated_data['title'],
            content = validated_data['content'],
            tags = validated_data['tags'],
            lite = validated_data['like']
        )

        return post


# post comment test 진행 
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'