from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/signup.html')

def login(request):
    return render(request, 'core/login.html')
