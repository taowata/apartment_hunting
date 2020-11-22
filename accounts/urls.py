from django.urls import path
from .views import registerfunc

app_name = 'accounts'
urlpatterns = [
    path('register/', registerfunc),
]
