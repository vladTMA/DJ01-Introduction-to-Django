# views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def neo(request):
    return render(request, "neo.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")
