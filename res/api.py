from .models import Todos
from .serializers import TodoSerializer

from rest_framework import viewsets, permissions

class TodoViewSet(viewsets.ModelViewSet):
    queryset= Todos.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= TodoSerializer