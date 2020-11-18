from django.views.generic import TemplateView


# Create your views here.

class ApartmentListView(TemplateView):
    template_name = "apartment/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = "お部屋リスト"
        return context
