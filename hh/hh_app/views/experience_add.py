from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from hh_app.forms import ExperienceForm
from hh_app.models import Experience
from hh_app.models import Resume


class ExperienceAddView(LoginRequiredMixin, CreateView):
    template_name = 'experience/experience_add.html'
    form_class = ExperienceForm
    model = Experience
    success_url = '/'

    def form_valid(self, form):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        education = form.save(commit=False)
        education.resume = resume
        education.save()
        return redirect('resume_update', pk=resume.pk)

    def get_context_data(self, *args, **kwargs):
        context = super(ExperienceAddView, self).get_context_data()
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        return context

