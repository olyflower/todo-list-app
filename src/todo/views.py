from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView

from todo.forms import TaskAddForm
from todo.models import Task


class IndexView(TemplateView):
    template_name = "../templates/index.html"


class ToDoListView(ListView):
    redirect_field_name = "todo:todo"
    template_name = '../templates/todo/todo.html'
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:todo')


class TaskAddView(CreateView):
    model = Task
    form_class = TaskAddForm
    success_url = reverse_lazy('todo:todo')
    template_name = '../templates/todo/todo.html'
