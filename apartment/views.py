from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Apartment


# Create your views here.

class ApartmentListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "apartment/list.html"
    model = Apartment
    context_object_name = 'apartment_list'
