from django.views.generic import DetailView
from hh_app.models import Vacancy


class VacancyDetailView(DetailView):
    template_name = "vacancies/vacancy.html"
    context_object_name = 'vacancy'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

