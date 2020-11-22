from django.urls import path
from .views import registerfunc
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'
urlpatterns = [
    path('register/', registerfunc),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
