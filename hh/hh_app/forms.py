from django import forms
from hh_app.models import Vacancy, VacancyCategory, Resume
from hh_app.models import Respond


class VacancyForm(forms.ModelForm):
    vacancy_category = forms.ModelChoiceField(
        required=True,
        label='Категория вакансии',
        queryset=VacancyCategory.objects.all(),
        initial=[0]
    )

    class Meta:
        model = Vacancy
        fields = (
            'name',
            'salary',
            'description',
            'experience_time',
            'is_public',
            'vacancy_category'
        )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск")


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            'salary_level',
            'info_user',
            'email',
            'phone',
            'telegram',
            'linkedin',
            'facebook'
        )


class RespondForm(forms.ModelForm):

    class Meta:
        model = Respond
        fields = (
            'resume',
        )

