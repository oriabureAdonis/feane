
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from posts.views import index, about, book, menu, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('book/', book),
    path('menu/', menu),
]

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
