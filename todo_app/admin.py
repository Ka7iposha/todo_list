from django.contrib import admin
from todo_app.models import ToDoItem, Todolist, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category,  CategoryAdmin)
admin.site.register(ToDoItem)
admin.site.register(Todolist)

