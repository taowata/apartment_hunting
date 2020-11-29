from django.urls import path
from .views import register_func, login_func, logout_func, guest_login_func
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'
urlpatterns = [
    path('register/', register_func, name='register'),
    path('login/', login_func, name='login'),
    path('logout/', logout_func, name='logout'),
    path('guest/',  guest_login_func, name='guest'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
