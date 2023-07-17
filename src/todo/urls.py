from django.urls import path

from .views import IndexView, ToDoListView, TaskDeleteView, TaskAddView

app_name = "todo"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("todo/", ToDoListView.as_view(), name="todo"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path("add/", TaskAddView.as_view(), name="add_task"),

]
