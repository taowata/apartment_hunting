from django.urls import path
from .views import register_func, login_func
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'
urlpatterns = [
    path('register/', register_func),
    path('login/', login_func),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
