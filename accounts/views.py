from django.views.generic import TemplateView


# Create your views here.

class RegisterView(TemplateView):
    template_name = "accounts/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["register"] = "ユーザー登録画面"
        return context
