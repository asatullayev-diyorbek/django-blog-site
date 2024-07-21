from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_urls
from config import settings

urlpatterns = [
    path('', include(blog_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
