from django.urls import path
from hh_app.views.vacancy_add import VacancyAddView
from hh_app.views.vacancy_detail import VacancyDetailView
from hh_app.views.vacancy_home import HomeVacancyView
from hh_app.views.vacancy_update import VacancyUpdateView, update_date, VacancyPublicUpdateView
from hh_app.views.resume_add import ResumeAddView
from hh_app.views.resume_home import HomeResumeView
from hh_app.views.resume_detail import ResumeDetailView
from hh_app.views.responde_add import RespondAddView
from hh_app.views.resume_update import update_date_resume, ResumePublicUpdateView, ResumeUpdateView
from hh_app.views.education_add import EducationAddView

urlpatterns = [
    path('', HomeVacancyView.as_view(), name='home'),
    path('vacancy/add', VacancyAddView.as_view(), name='vacancy_add'),
    path('vacancy/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/update/<int:pk>', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/update/date/<int:pk>', update_date, name='vacancy_update_date'),
    path('vacancy/update/public/<int:pk>', VacancyPublicUpdateView.as_view(), name='vacancy_update_public'),
    
    path('resume/add/', ResumeAddView.as_view(), name='resume_add'),
    path('resume/list/', HomeResumeView.as_view(), name='resume_home'),
    path('resume/<int:pk>', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/update/<int:pk>', ResumeUpdateView.as_view(), name='resume_update'),
    path('resume/update/date/<int:pk>', update_date_resume, name='resume_update_date'),
    path('resume/update/public/<int:pk>', ResumePublicUpdateView.as_view(), name='resume_update_public'),

    path('resume/<int:pk>/education/add/', EducationAddView.as_view(), name='education_add'),

    path('respond/add/<int:pk>', RespondAddView.as_view(), name='respond_add'),
    ]

