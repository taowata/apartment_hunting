from django.views.generic import ListView
from .models import Apartment


# Create your views here.

class ApartmentListView(ListView):
    template_name = "apartment/list.html"
    model = Apartment
    context_object_name = 'apartment_list'
