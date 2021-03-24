from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('managers/', include('django.contrib.auth.urls')),
    path('managers/', include('managers.urls')),
    path('', include('main.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'main.views.error_404_view'