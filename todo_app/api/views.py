from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from todo_app.api.serializers import UserSerializer, TodolistSerializer, ToDoItemSerializer
from todo_app.models import Todolist, ToDoItem


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    permission_classes = [permissions.IsAuthenticated]


class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

