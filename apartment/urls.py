from django.urls import path
from .views import ApartmentListView, detail_func
from django.conf import settings
from django.conf.urls.static import static


app_name = 'apartment'
urlpatterns = [
    path('list', ApartmentListView.as_view()),
    path('detail/<int:pk>', detail_func, name='detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
