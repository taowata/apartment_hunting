from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Apartment, Room


# Create your views here.

class ApartmentListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "apartment/list.html"
    model = Apartment
    context_object_name = 'apartment_list'


def detail_func(request, pk):
    room_object = Room.objects.get(pk=pk)
    return render(request, 'apartment/detail.html', {'room_object': room_object})
