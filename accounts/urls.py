from django.urls import path
from .views import register_func, login_func, logout_func, guest_login_func, add_favorite_apartment_func, \
    remove_favorite_apartment_func, mypage_func
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
                  path('', login_func),
                  path('register/', register_func, name='register'),
                  path('login/', login_func, name='login'),
                  path('logout/', logout_func, name='logout'),
                  path('guest/', guest_login_func, name='guest'),
                  path('like/', add_favorite_apartment_func, name='like'),
                  path('not_like/', remove_favorite_apartment_func, name='not_like'),
                  path('mypage/', mypage_func, name='my_page'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
