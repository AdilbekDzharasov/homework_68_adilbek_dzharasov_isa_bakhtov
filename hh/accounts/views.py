from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from accounts.forms import LoginForm, CustomUserCreationForm
from django.core.paginator import Paginator


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
        pk = form.cleaned_data.get('pk')
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


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'account.html'
    context_object_name = 'user_obj'
    paginate_related_by = 3
    paginate_related_orphans = 0

