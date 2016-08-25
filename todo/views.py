from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import loader 
from django.urls import reverse
from django.views import generic
from .models import Post, Choice
import random

# class IndexView(generic.ListView):
#     template_name='todo/index.html'
#     context_object_name = 'latest_question_list'
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Post.objects.order_by('?')[:5]

# class DetailView(generic.DetailView):
#     model = Post 
#     template_name = 'todo/detail.html'

# class ResultsView(generic.DetailView):
#     model = Post 
#     template_name = 'todo/results.html'

# def vote(request, question_id):
#     post = get_object_or_404(Post, pk=question_id)

#     try:
#         selected_choice = post.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'todo/detail.html', {
#             'post': post,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('todo:results', args=(post.id,)))


#==================================================================

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
    return render(request, 'todo/detail.html', {'post': post})

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

def vote(request, question_id):
    post = get_object_or_404(Post, pk=question_id)
    print("vote()")
    try:
        selected_choice = post.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'todo/detail.html', {
            'post': post,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print("save")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('todo:results', args=(post.id,)))

def results(request, question_id):
    question = get_object_or_404(Post, pk=question_id)
    return render(request, 'todo/results.html', {'question': question})