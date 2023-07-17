from django import forms
from .models import Task


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "due_date"]