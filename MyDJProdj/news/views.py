# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news/home.html', {'news': news})

def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    return render(request, 'news/detail.html', {'item': item})
