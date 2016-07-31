#from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from django.views.generic.edit import UpdateView
from django.forms import modelform_factory
from django.forms import Textarea

from .models import Task
from .forms import AddTaskForm
from .forms import UpdateTaskForm

def test(request):
	helloWorld = "Hello world!!"
	return HttpResponse(helloWorld)

def get_newtask(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
        	Task.objects.create(
        		task_title = form.cleaned_data['input_title'], 
        		task_detail = form.cleaned_data['input_detail'])
        	return HttpResponseRedirect(reverse('tasks:tasklist'))
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add.html', {'form': form})

def update(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            task.task_status = form.cleaned_data['task_status']
            task.save()
            return HttpResponseRedirect(reverse('tasks:tasklist'))
    else:
        task = get_object_or_404(Task, pk=pk)
        form = UpdateTaskForm(instance=task)
    return render(request, 'tasks/update.html', {'form':form, 'task':task})
    
class TasklistView(generic.ListView):
	template_name = 'tasks/tasklist.html'
	context_object_name = 'tasklist'
	def get_queryset(self):
		return Task.objects.all()

class DetailView(generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'



