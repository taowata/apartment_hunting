from django.urls import path
from .views import ApartmentListView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'apartment'
urlpatterns = [
    path('list', ApartmentListView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
