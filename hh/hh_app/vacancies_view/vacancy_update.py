from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, FormView
from hh_app.forms import VacancyForm
from hh_app.models import Vacancy


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancies/update.html'
    form_class = VacancyForm
    model = Vacancy
    context_object_name = 'vacancy'

    def get_success_url(self):
        return reverse('home')


def update_date(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.save()
    return redirect('vacancy_detail', vacancy.pk)

