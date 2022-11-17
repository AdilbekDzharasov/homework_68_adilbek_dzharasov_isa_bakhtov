from django.urls import path
from hh_app.vacancies_view.vacancy_add import VacancyAddView
from hh_app.vacancies_view.vacancy_detail import VacancyDetailView
from hh_app.vacancies_view.vacancy_home import HomeVacancyView
from hh_app.vacancies_view.vacancy_update import VacancyUpdateView, update_date

urlpatterns = [
    path('', HomeVacancyView.as_view(), name='home'),
    path('vacancy/add', VacancyAddView.as_view(), name='vacancy_add'),
    path('vacancy/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/update/<int:pk>', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/update/date/<int:pk>', update_date, name='vacancy_update_date'),
    # path('like/<int:pk>', LikeView, name='like_post')
    ]

