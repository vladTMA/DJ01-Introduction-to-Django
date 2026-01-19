# main/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.CharField(
        max_length=250,
        blank=True,
        null=True,  # ← ЭТО НУЖНО
        verbose_name="Подзаголовок"
    )
    content = models.TextField(verbose_name="Содержимое")

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор"
    )

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, max_length=250, verbose_name="URL", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.slug])

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField("Название книги", max_length=200)
    author = models.CharField("Автор",max_length=200)
    description = models.TextField("Описание")
    review = models.TextField("Отзыв")
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    image = models.ImageField(
        upload_to="books/",
        blank=True,
        null=True,
        verbose_name="Обложка"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


    def __str__(self):
        return self.title
