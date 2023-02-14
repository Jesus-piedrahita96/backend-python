from .models import Todos, Menu, Post
from .serializers import TodoSerializer, MenuSerializer, PostSerializer

from rest_framework import viewsets, permissions


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MenuSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
