# main/views.py

from pathlib import Path
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from news.models import News
from .forms import BookForm, ArticleForm, CustomUserRegistrationForm, CustomLoginForm
from .models import Article, Book, CustomUser


# -----------------------------
# Регистрация пользователя
# -----------------------------
class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# -----------------------------
# Вход пользователя
# -----------------------------
class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomLoginForm


# -----------------------------
# Главные страницы
# -----------------------------
def index(request):
    latest_news = News.objects.order_by('-created_at')[:3]
    return render(request, "main/index.html", {"latest_news": latest_news})


def about(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")


# -----------------------------
# Статьи
# -----------------------------
def articles(request):
    article_list = Article.objects.filter(is_published=True).order_by("-created_at")
    paginator = Paginator(article_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "main/articles.html", {"page_obj": page_obj})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "main/article_detail.html", {"article": article})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        # Предпросмотр
        if "preview" in request.POST:
            if form.is_valid():
                preview_article = form.save(commit=False)
                return render(
                    request,
                    "main/article_preview.html",
                    {"article": preview_article, "preview": True}
                )

        # Сохранение
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", slug=article.slug)

    else:
        form = ArticleForm()

    return render(
        request,
        "main/article_form.html",
        {"form": form, "title": "Добавить статью"}
    )


def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_detail", slug=article.slug)
    else:
        form = ArticleForm(instance=article)

    return render(
        request,
        "main/article_form.html",
        {"form": form, "title": "Редактировать статью"}
    )


def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        article.delete()
        return redirect("articles")

    return render(request, "main/article_delete_confirm.html", {"article": article})


# -----------------------------
# Книги
# -----------------------------
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "main/add_book.html", {"form": form})


def book_list(request):
    books = Book.objects.order_by("-created_at")
    return render(request, "main/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "main/book_detail.html", {"book": book})


# -----------------------------
# Страница NEO (защищена)
# -----------------------------
@login_required
def neo(request):
    project_root = Path(__file__).resolve().parent.parent  # папка с manage.py

    models_code = (project_root / "main" / "models.py").read_text(encoding="utf-8")
    views_code = (project_root / "main" / "views.py").read_text(encoding="utf-8")
    urls_code = (project_root / "main" / "urls.py").read_text(encoding="utf-8")

    run_bat = (project_root / "run_django.bat").read_text(encoding="utf-8")
    stop_bat = (project_root / "stop_django.bat").read_text(encoding="utf-8")

    return render(
        request,
        "main/neo.html",
        {
            "models_code": models_code,
            "views_code": views_code,
            "urls_code": urls_code,
            "run_bat": run_bat,
            "stop_bat": stop_bat,
        }
    )
