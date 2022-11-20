from django.views.generic import DetailView
from hh_app.models import Resume


class ResumeDetailView(DetailView):
    template_name = "resume/resume_detail.html"
    context_object_name = 'resume'
    model = Resume

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeDetailView, self).get_context_data(object_list=object_list, **kwargs)
        resume = self.object
        educations = resume.education
        context['educations'] = educations
        experiences = resume.experience
        context['experiences'] = experiences
        return context


        
