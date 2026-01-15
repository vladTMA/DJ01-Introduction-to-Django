# views.py
from django.shortcuts import render, get_object_or_404
from news.models import News
from .models import Article

# Create your views here.

def index(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, "main/index.html",{"latest_news": latest_news})

def neo(request):
    return render(request, "main/neo.html")

def about(request):
    return render(request, "main/about.html")

def contacts(request):
    return render(request, "main/contacts.html")

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, "main/article_list.html", {"articles": articles})

def article_detail(request, pk):
    item = get_object_or_404(Article, pk=pk)
    return render(request, "main/article_detail.html", {"item": item})

def articles(request):
    items = Article.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "main/articles.html", {"items": items})

def home(request):
    return render(request, "main/home.html")

def index(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, "main/index.html", {"latest_news": latest_news})

def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/home.html', {'news': news})
