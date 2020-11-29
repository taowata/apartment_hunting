from django.urls import path
from . import views

app_name = 'import_records'

urlpatterns = [
    path('', views.ApartmentList.as_view(), name='index'),
    path('import/', views.RecordsImport.as_view(), name='import'),
    path('export/', views.post_export, name='export'),
]