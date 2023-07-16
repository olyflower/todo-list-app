from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView

from todo.models import Task


class IndexView(TemplateView):
    template_name = "../templates/index.html"


class ToDoListView(ListView):
    redirect_field_name = "index"
    template_name = '../templates/todo/todo.html'
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:todo')
