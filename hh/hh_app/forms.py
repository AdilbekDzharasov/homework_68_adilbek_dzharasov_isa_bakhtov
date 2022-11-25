from django import forms
from hh_app.models import Vacancy, VacancyCategory, Resume, Respond, Education, Experience, Message
from hh_app.widgets import DatePickerInput


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


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'message',
        )


class EducationForm(forms.ModelForm):
    begin_date = forms.DateField(required=True, label='Beginning date', widget=DatePickerInput)
    end_date = forms.DateField(required=False, label='Expiration date', widget=DatePickerInput)

    class Meta:
        model = Education
        fields = (
            'institution_name',
            'speciality',
            'category_education',
            'begin_date',
            'end_date',
            'faculty'
        )


class ExperienceForm(forms.ModelForm):
    begin_date = forms.DateField(required=True, label='Beginning date', widget=DatePickerInput)
    end_date = forms.DateField(required=False, label='Expiration date', widget=DatePickerInput)

    class Meta:
        model = Experience
        fields = (
            'company',
            'job_title',
            'begin_date',
            'end_date',
        )

