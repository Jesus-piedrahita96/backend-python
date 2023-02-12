from .models import Todos
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todos
        fields= ('id', 'text', 'create_at', 'completed')
        read_only_fields= ('create_at',)
