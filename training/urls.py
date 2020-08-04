from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ltwg_do6_sfg/', admin.site.urls),
    path('', include('main.urls', namespace='')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.THUMBNAIL_MEDIA_URL, document_root=settings.THUMBNAIL_MEDIA_ROOT)
