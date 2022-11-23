from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from hh_app.models import Respond
from hh_app.forms import RespondForm
from hh_app.models import Vacancy


class RespondAddView(CreateView):
    model = Respond
    template_name = 'respond/add.html'
    form_class = RespondForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.vacancy = get_object_or_404(Vacancy,  pk=self.kwargs.get('pk'))
        return super().form_valid(form)

