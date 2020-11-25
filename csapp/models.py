from django.db import models

class MyTasks(models.Model):
	task_name = models.CharField(max_length=100)

	def __str__(self):
		return self.task_name