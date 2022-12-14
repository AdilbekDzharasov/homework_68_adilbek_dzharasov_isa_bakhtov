from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from accounts.forms import LoginForm, CustomUserCreationForm
from django.core.paginator import Paginator
from accounts.forms import UserChangeForm
from django.urls import reverse


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        user = authenticate(request, email=email, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class EmployerDetailView(DetailView):
    model = get_user_model()
    template_name = 'employer/office_employer.html'
    context_object_name = 'account'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        vacancies = self.get_object().vacancies_view.all()
        messages = self.get_object().message.all()
        paginator = Paginator(vacancies, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['vacancies'] = page.object_list
        kwargs['messages'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class CompanyDetailView(DetailView):
    model = get_user_model()
    template_name = 'employer/company_detail.html'
    context_object_name = 'account'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        vacancies = self.get_object().vacancies_view.all()
        paginator = Paginator(vacancies, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['vacancies'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class ApplicantDetailView(DetailView):
    model = get_user_model()
    template_name = 'applicant/office_applicant.html'
    context_object_name = 'account'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        resumes = self.get_object().resumes.all()
        responses = self.get_object().responses.all()
        paginator = Paginator(resumes, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['resumes'] = page.object_list
        kwargs['responses'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class AccountChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('account_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

