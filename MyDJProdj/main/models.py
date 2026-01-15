# main/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    subtitle = models.CharField("Подзаголовок", max_length=250, blank=True)
    content = models.TextField("Содержимое")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор"
    )

    is_published = models.BooleanField("Опубликовано", default=True)

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.pk])

    def __str__(self):
        return self.title
