from django.urls import include, path
from rest_framework import routers
from todo_app.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todolist', views.TodolistViewSet)
router.register(r'todo-item', views.ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

