from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE),
    title = models.CharField(max_length=50)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
