from rest_framework import serializers
from django.contrib.auth.models import User
from apps.myblog.models import Comment, Post

from rest_framework.fields import CurrentUserDefault

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

#coba dari post
class CreatePostSerializer(serializers.ModelSerializer):
    #field pada models bisa diganti2 pada serilizers
    author = serializers.CharField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'title','image','content', 'date_posted','author')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)

        return post

class PostSerializer(serializers.ModelSerializer):
    #field pada models bisa diganti2 pada serilizers
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['title','image','content', 'date_posted', 'author', 'likes','dislikes']


