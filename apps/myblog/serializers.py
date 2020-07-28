from rest_framework import serializers
from .models import Comment, Post
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault

class PostSerializer(serializers.ModelSerializer):
    #field pada models bisa diganti2 pada serilizers
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['title','image','content', 'date_posted', 'author', 'likes','dislikes']

class CreatePostSerializer(serializers.ModelSerializer):
    #field pada models bisa diganti2 pada serilizers
    author = serializers.CharField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'title','image','content', 'date_posted','author')

    # def create(self, validated_data):
    #     post = Post.objects.create(**validated_data)

    #     return post











































    # def create(self, validated_data):
    #     post = Post.objects.create(validated_data['title'], validated_data['image'], validated_data['content'])
    #     return post

# class PostSerializer(serializers.Serializer):
#     image = serializers.ImageField(default='default.png')
#     title = serializers.CharField(max_length=200, default='')
#     content = serializers.CharField(max_length=2000)
#     date_posted = serializers.DateTimeField()
#     author = serializers.ForeignKey(User, on_delete=models.CASCADE)
#     likes= serializers.IntegerField(default=0)
#     dislikes= serializers.IntegerField(default=0) 

#     def create(self, validated_data):
#         return Post.objects.create(validated_data)   
    
#     def update(self, instance, validated_data):
#         instance.image = validated_data.get('image', instance.image)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.date_posted = validated_data.get('date_posted', instance.date_posted)
#         instance.author = validated_data.get('author', instance.author)
#         instance.likes = validated_data.get('likes', instance.likes)
#         instance.dislikes = validated_data.get('dislikes', instance.dislikes)
#         instance.save()
#         return instance