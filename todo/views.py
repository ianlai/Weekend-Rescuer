from django.shortcuts import render

from django.http import HttpResponse
import random

def home(request):
    testmessage="Weekend Rescuer!"

    print(testmessage) 
    return HttpResponse(testmessage)
    #return render(request, 'index.html', {"text":testmessage}) 

