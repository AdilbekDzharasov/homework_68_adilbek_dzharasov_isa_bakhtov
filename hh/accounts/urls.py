from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, EmployerDetailView, AccountChangeView, ApplicantDetailView, CompanyDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('employer/detail/<int:pk>', EmployerDetailView.as_view(), name='account_detail'),
    path('company/detail/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('applicant/detail/<int:pk>', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('account/<int:pk>/change', AccountChangeView.as_view(), name='account_change')
]

