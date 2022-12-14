from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from hh_app.models import Vacancy
from hh_app.forms import VacancyForm


class VacancyAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'vacancies/add.html'
    form_class = VacancyForm
    permission_required = 'hh_app.add_vacancy'

    def get_success_url(self):
        return reverse('vacancy_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

