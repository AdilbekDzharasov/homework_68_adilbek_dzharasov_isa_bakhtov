from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from hh_app.models import Resume
from hh_app.forms import ResumeForm


class ResumeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'resume/resume_update.html'
    form_class = ResumeForm
    model = Resume
    context_object_name = 'resume'

    def get_success_url(self):
        return reverse('resume_home')


def update_date_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.save()
    return redirect('resume_detail', resume.pk)


class ResumePublicUpdateView(LoginRequiredMixin, UpdateView):
    model = Resume
    template_name = 'resume/update_public.html'
    fields = ['is_public']

    def get_success_url(self):
        return reverse('home')

