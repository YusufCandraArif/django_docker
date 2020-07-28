from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer, CreatePostSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# def post_list(request):
#     if request.method == 'GET':
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         return JsonResponse(serializer.data, safe=False)


 
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
 
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
 
    def get(self, request, id = None):
        return self.list(request)
        
    # def post(self, request):
    #     return self.create(request)

class GenericAPIViewDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
 
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
 
    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
 
    def put(self, request, id=None):
        return self.update(request, id)
 
    def delete(self, request, id):
        post = Post.objects.get(id=id)
        if post:
            author = post.author
            if author == request.user:
                return self.destroy(request, id)
        return "Salah"

# class GenericAPIViewCreatePost(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = CreatePostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'
 
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     #authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]


#     def post(self, request):
#         CreatePostSerializer.set_author(request.user)
#         return self.create(request)

class GenericAPIViewCreatePost(generics.GenericAPIView):
    serializer_class = CreatePostSerializer
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [BasicAuthentication]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response({
        "data": CreatePostSerializer(post, context=self.get_serializer_context()).data
        })