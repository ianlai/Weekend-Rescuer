#from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Task
from .forms import AddTaskForm

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
        	#return render(request, 'tasks/tasklist.html', {'form': form})
        	return HttpResponseRedirect(reverse('tasks:tasklist'))
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add.html', {'form': form})
    
class TasklistView(generic.ListView):
	template_name = 'tasks/tasklist.html'
	context_object_name = 'tasklist'
	def get_queryset(self):
		return Task.objects.all()

class DetailView(generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'
