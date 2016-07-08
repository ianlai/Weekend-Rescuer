from django.db import models

class Task(models.Model):

	STATUS_CHOICES = (
		('TODO', 'TODO'),
		('DONE', 'DONE'),
	)
	task_status = models.CharField(
		max_length=4,
		choices = STATUS_CHOICES,
		default = 'TODO'
	)

	task_title = models.CharField(max_length=100)

	task_detail = models.CharField(max_length=500)

	def __str__(self):
		return self.task_title
