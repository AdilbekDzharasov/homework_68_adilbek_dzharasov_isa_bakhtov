from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from hh_app.models import Resume
from hh_app.forms import ResumeForm


class ResumeAddView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('resume_update', pk=resume.pk)

