from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=50)
    mustDo = models.TextField()
    couldDo = models.TextField()
    if_IhaveTime = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    self.title