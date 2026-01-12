# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def neo(request):
    return render(request, "main/neo.html")

def about(request):
    return render(request, "main/about.html")

def contacts(request):
    return render(request, "main/contacts.html")

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "main/article_detail.html", {"article": article})

def article_list(request):
    return render(request, "main/article_list.html")
