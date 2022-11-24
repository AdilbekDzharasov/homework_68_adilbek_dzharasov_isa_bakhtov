from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from hh_app.forms import VacancyForm
from hh_app.models import Vacancy


class VacancyUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'vacancies/update.html'
    form_class = VacancyForm
    model = Vacancy
    context_object_name = 'vacancy'
    permission_required = 'hh_app.change_vacancy'

    def get_success_url(self):
        return reverse('home')

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


def update_date(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.save()
    return redirect('vacancy_detail', vacancy.pk)


class VacancyPublicUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Vacancy
    template_name = 'vacancies/update_public.html'
    fields = ['is_public']
    permission_required = 'hh_app.change_vacancy'

    def get_success_url(self):
        return reverse('home')

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

