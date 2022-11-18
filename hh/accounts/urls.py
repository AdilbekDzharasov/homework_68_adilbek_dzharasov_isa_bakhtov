from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, EmployerDetailView, AccountChangeView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('account/detail/<int:pk>', EmployerDetailView.as_view(), name='account_detail'),
    path('account/<int:pk>/change', AccountChangeView.as_view(), name='account_change')
    # path('account/password_change', AccountPasswordChangeView.as_view(), name='password_change')
]

