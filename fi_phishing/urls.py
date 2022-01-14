from django.contrib import admin, staticfiles
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phishing.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
