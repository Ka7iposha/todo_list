from django.contrib import admin
from todo_app.models import ToDoItem, Todolist

admin.site.register(ToDoItem)
admin.site.register(Todolist)

