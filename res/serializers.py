from .models import Todos, Menu, Post
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ('id', 'text', 'create_at', 'completed')
        read_only_fields = ('create_at',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'to', 'text', 'private')
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'auth', 'content', 'slug', 'title')
        read_only_fields = ('id',)
