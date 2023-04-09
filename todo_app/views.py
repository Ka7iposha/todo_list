from django.views.generic import ListView
from .models import Todolist, ToDoItem


class ListListView(ListView):
    model = Todolist
    template_name = "todo_app/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

