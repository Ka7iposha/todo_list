from django.contrib.auth.models import User
from rest_framework import serializers
from todo_app.models import Todolist, ToDoItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TodolistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todolist
        fields = ['title']


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'created_date', 'due_date']

