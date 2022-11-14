from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    # path('account/detail/<int:pk>', AccountDetailView.as_view(), name='account_detail'),
    # path('account/<int:pk>/change', AccountChangeView.as_view(), name='change'),
    # path('account/password_change', AccountPasswordChangeView.as_view(), name='password_change')
]

