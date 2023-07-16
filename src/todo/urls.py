from django.urls import path

from todo.views import IndexView, ToDoListView, TaskDeleteView

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("todo/", ToDoListView.as_view(), name="todo"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
