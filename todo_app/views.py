from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todolist, ToDoItem
from django.urls import reverse, reverse_lazy


class ListListView(ListView):
    model = Todolist
    template_name = "todo_app/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = Todolist.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = Todolist
    fields = ["title"]
    template_name = "todo_app/todo_list_form.html"

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Добавить новый список"
        return context


class ItemCreate(CreateView):
    model = ToDoItem
    fields = ["todo_list", "category", "title", "description", "due_date", "complete"]
    template_name = "todo_app/todo_item_form.html"

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = Todolist.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = Todolist.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Создать новую задачу"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = ["todo_list", "category", "title", "description", "due_date", "complete"]
    template_name = "todo_app/todo_item_form.html"

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Редактировать задачу"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDelete(DeleteView):
    model = Todolist
    success_url = reverse_lazy("index")


class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context

