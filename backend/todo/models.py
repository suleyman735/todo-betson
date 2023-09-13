from django.db import models

from django.utils import timezone


# Create your models here.


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateField()
    due_date = models.DateField()
    
    done = models.BooleanField()


    def __str__(self):
        return f"{self.title}: due {self.due_date}"