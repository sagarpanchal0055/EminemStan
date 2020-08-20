from django.shortcuts import render, redirect
# from .models import 

# Create your views here.


def index(request):
    return render( request, 'index.html')


def home(request):
    return render( request, 'index.html')


def about(request):
    return render( request, 'about.html')
