from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from hh_app.models import Resume, Education, Experience


class ResumeDetailView(DetailView):
    template_name = "resume/resume_detail.html"
    context_object_name = 'resume'
    model = Resume
    pk_url_kwarg = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeDetailView, self).get_context_data(object_list=object_list, **kwargs)
        resume = self.object
        educations = Education.objects.filter(resume_id = self.kwargs['pk'])
        context['educations'] = educations
        experiences = Experience.objects.filter(resume_id = self.kwargs['pk'])
        context['experiences'] = experiences
        
        return context


        
