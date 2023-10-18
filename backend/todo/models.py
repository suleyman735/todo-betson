from django.db import models

from django.utils import timezone


# Create your models here.


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField('Created',)

    due_date = models.DateTimeField('Will Finish',)
    
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title