from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from hh_app.forms import EducationForm
from hh_app.models import Education
from hh_app.models import Resume


class EducationAddView(CreateView):
    template_name = 'education/education_add.html'
    form_class = EducationForm
    model = Education
    success_url = '/'

    def form_valid(self, form):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        education = form.save(commit=False)
        education.resume = resume
        education.save()
        return redirect('resume_update', pk=resume.pk)

    def get_context_data(self, *args, **kwargs):
        context = super(EducationAddView, self).get_context_data()
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        return context

