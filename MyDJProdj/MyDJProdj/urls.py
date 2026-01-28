from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.admin

urlpatterns = [
    path("admin/", main.admin.admin_site.urls),
    path("", include("main.urls")),
    path("news/", include("news.urls")),
    path("api/", include("bot.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
