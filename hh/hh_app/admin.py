from django.contrib import admin
from hh_app.models import Vacancy, VacancyCategory, Resume, Education, Experience


# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     list_filter = ['id', 'name']
#     search_fields = ['id', 'name']
#     fields = ['name']
#     readonly_fields = ['id']

admin.site.register(Vacancy)

admin.site.register(VacancyCategory)

admin.site.register(Resume)

admin.site.register(Education)

admin.site.register(Experience)
