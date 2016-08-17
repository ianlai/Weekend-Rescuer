from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader 
from .models import Post
import random

def home(request):
    testmessage="Weekend Rescuer!"

    print(testmessage) 
    return HttpResponse(testmessage)
    #return render(request, 'index.html', {"text":testmessage}) 

def detail(request, question_id):
    #try:
    #    post = Post.objects.get(pk=question_id)
    #except Post.DoesNotExist:
    #    raise Http404("!!! Post does not exist")
    #return HttpResponse("Post (id=%(id)s) : %(title)s" %
    #    {'id': question_id, 'title':post.title})
    
    post = get_object_or_404(Post, pk=question_id)
    return render(request, 'todo/detail.html', {'p': post})

def index(request):
    post_list = Post.objects.all().order_by('?')[:5]
    latest_question_list=post_list
    
    # Method1 
    # output = ', '.join([q.title for q in post_list]) #hard-code
    # return HttpResponse(output)
    
    # Method2
    #template = loader.get_template('todo/index.html')
    #context = {
    #    'latest_question_list' : latest_question_list,
    #}
    #return HttpResponse(template.render(context,request))

    # Method3 
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'todo/index.html', context) 
