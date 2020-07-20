from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import random


def index(request):
    context = {
        'numbers' : [
            { 'n1' : random.sample(range(1,46),1).pop() }, 
            { 'n2' : random.sample(range(1,46),1).pop() },
            { 'n3' : random.sample(range(1,46),1).pop() },
            { 'n4' : random.sample(range(1,46),1).pop() }, 
            { 'n5' : random.sample(range(1,46),1).pop() },
            { 'n6' : random.sample(range(1,46),1).pop() },
              ]
    }
    
    return render (request, 'lotto/index.html', context)
    
