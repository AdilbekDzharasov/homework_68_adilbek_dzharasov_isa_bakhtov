from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView
from hh_app.models import Respond
from hh_app.forms import MessageForm
from hh_app.models import Vacancy
from hh_app.models import Message


class MessageRespondAddView(LoginRequiredMixin, FormView):
    form_class = MessageForm

    def post(self, request, *args, **kwargs):
        respond = get_object_or_404(Respond, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get('message')
            author = request.user
            Message.objects.create(author=author, respond=respond, message=message)
        return redirect('home')


class VacancyRespondDetailView(LoginRequiredMixin, DetailView):
    model = Vacancy
    context_object_name = 'vacancy'
    template_name = 'respond/respond.html'

    def get_context_data(self, *args, **kwargs):
        context = super(VacancyRespondDetailView, self).get_context_data(*args, **kwargs)
        context['responses'] = self.object.responses.order_by('author')
        context['favorite_form'] = MessageForm()
        return context

