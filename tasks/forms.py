from django import forms
from django.forms import ModelForm

from .models import Task

class AddTaskForm(forms.Form):
     input_title = forms.CharField(label='Title', max_length=100)
     input_detail = forms.CharField(label='Detail', max_length=500)

class UpdateTaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['task_status']

