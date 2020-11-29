import csv
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .forms import CSVUploadForm
from apartment.models import Apartment, Room


class ApartmentList(generic.ListView):
    template_name = 'import_records/records_list.html'
    model = Apartment
    context_object_name = 'apartment_list'


class RecordsImport(generic.FormView):
    template_name = 'import_records/import.html'
    success_url = reverse_lazy('import_records:index')
    form_class = CSVUploadForm

    def form_valid(self, form):
        form.save()
        return redirect('import_records:index')


def post_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response)
    for apartment in Apartment.objects.all():
        writer.writerow([apartment.name, apartment.goodNumber])
    return response
