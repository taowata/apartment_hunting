from django.urls import path
from .views import ApartmentListView

app_name = 'apartment'
urlpatterns = [
    path('list', ApartmentListView.as_view()),
]
