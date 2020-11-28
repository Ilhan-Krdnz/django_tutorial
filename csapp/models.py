from django.db import models
from django.contrib.auth.models import User

class MyTasks(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task_name = models.CharField(max_length=100)

    def __str__(self):
        return self.task_name