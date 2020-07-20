from django.shortcuts import render
from .models import Login


# Create your views here.

from django.http import HttpResponse

def index(request):
    login = Login.objects.all()
    context = { 'logins' : login } 
    return render(request, 'login/index.html', context)

def detail(request, login_id):
    login = Login.objects.get(id=login_id)
    context = { 'logins' : login }
    return render(request, 'login/detail.html', context)

