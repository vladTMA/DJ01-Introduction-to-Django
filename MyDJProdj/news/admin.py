from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "short_description", "content")
    ordering = ("-created_at",)

    change_list_template = "admin/news/news/change_list.html"

    def save_model(self, request, obj, form, change):
        if not obj.author:          # если автор ещё не указан
            obj.author = request.user
        super().save_model(request, obj, form, change)




