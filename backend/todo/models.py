from django.db import models

from django.utils import timezone


# Create your models here.


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    done = models.BooleanField()
    # todo_list = models.ForeignKey(on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse(
    #         "item-update", args=[str(self.todo_list.id), str(self.id)]
    #     )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"