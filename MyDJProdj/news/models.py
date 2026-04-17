# news/models.py
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField('Название новости', max_length=75)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор"
    )

    def get_delete_url(self):
        return reverse("admin:news_news_delete", args=[self.pk])

    def __str__(self):
        return self.title



