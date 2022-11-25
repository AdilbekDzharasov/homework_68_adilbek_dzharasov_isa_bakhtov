from django.views.generic import ListView
from django.db.models import Q
from django.utils.http import urlencode
from hh_app.models import Resume
from hh_app.forms import SearchForm


class HomeResumeView(ListView):
    template_name = 'resume/resume_home.html'
    context_object_name = 'resumes'
    model = Resume
    ordering = ('-created_at')

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeResumeView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_public=True)
        if self.search_value:
            query = Q(email__icontains=self.search_value) | Q(info_user__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

