from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, CreatePostSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from apps.myblog.models import Comment, Post
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import action

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# class GenericAPIViewCreatePostKnox(viewsets.ModelViewSet):
#     serializer_class = CreatePostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return self.request.user
#         .all()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices = Post.objects.filter(question=question)
        serializer = CreatePostSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = CreatePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)

class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Get Update Delete """
    serializer_class = CreatePostSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self, id=None):
        return Post.objects.filter(id=id).order_by('-date_posted')