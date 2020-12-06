from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Apartment, Room


# Create your views here.

class ApartmentListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "apartment/list.html"
    model = Apartment
    removed_room_id = set()
    context_object_name = 'apartment_list'

    def get_queryset(self):
        results = self.model.objects.all()
        self.removed_room_id.clear()

        q_age = self.request.GET.get('age')
        q_layout = self.request.GET.get('layout')
        q_rent_bottom = self.request.GET.get('rent_bottom')
        q_rent_top = self.request.GET.get('rent_top')
        q_separated_bathroom = str(self.request.GET.get('separated_bathroom'))
        q_available = str(self.request.GET.get('available'))

        if not q_age:
            pass
        elif q_age.isnumeric():
            results = results.filter(age__lte=int(q_age))

        if not q_layout:
            pass
        elif q_layout == "1room":
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.floorPlan == "ワンルーム":
                        self.removed_room_id.add(room.id)
        elif q_layout == "1k":
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.floorPlan == "1K":
                        self.removed_room_id.add(room.id)

        if not q_rent_bottom:
            pass
        elif q_rent_bottom.isnumeric():
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.rent >= int(q_rent_bottom):
                        self.removed_room_id.add(room.id)

        if not q_rent_top:
            pass
        elif q_rent_top.isnumeric():
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.rent <= int(q_rent_top):
                        self.removed_room_id.add(room.id)

        if not q_separated_bathroom:
            pass
        elif q_separated_bathroom == "on":
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.areBathAndToiletSeparated:
                        self.removed_room_id.add(room.id)

        if not q_available:
            pass
        elif q_available == "on":
            for apartment in results:
                for room in apartment.room_set.all():
                    if not room.isRentable:
                        self.removed_room_id.add(room.id)

        for apartment in results:
            has_rooms = False
            for room in apartment.room_set.all():
                if room.id in self.removed_room_id:
                    pass
                else:
                    has_rooms = True
                    break
            if not has_rooms:
                results = results.exclude(name=apartment.name)
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['removed_room_id'] = self.removed_room_id
        return context


def detail_func(request, pk):
    room_object = Room.objects.get(pk=pk)
    return render(request, 'apartment/detail.html', {'room_object': room_object})
