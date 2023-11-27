from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("todo:task-detail", args=[self.object.pk])


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")
