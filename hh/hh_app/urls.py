from django.urls import path
from hh_app.vacancies_view.vacancy_add import VacancyAddView
from hh_app.vacancies_view.vacancy_detail import VacancyDetailView
from hh_app.vacancies_view.vacancy_home import HomeVacancyView


urlpatterns = [
    path('', HomeVacancyView.as_view(), name='home'),
    path('vacancy/add', VacancyAddView.as_view(), name='vacancy_add'),
    path('vacancy/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    # path('add/comment/<int:pk>', CommentAddView.as_view(), name='to_comment'),
    # path('like/<int:pk>', LikeView, name='like_post')
    ]

