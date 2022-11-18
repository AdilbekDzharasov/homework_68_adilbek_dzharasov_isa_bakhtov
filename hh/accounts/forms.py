from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from accounts.models import Role


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Email'
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )


class CustomUserCreationForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('O', 'Другое'),
        ('M', "Мужской"),
        ('W', "Женский"),
    )

    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Повторите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    username = forms.CharField(label='Имя')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Пол')
    role = forms.ModelChoiceField(required=True, label='Роль', queryset=Role.objects.all(), initial=[0])

    class Meta:
        model = get_user_model()
        fields = (
            'role',
            'email',
            'username',
            'photo',
            'password',
            'password_confirm',
            'phone',
            'gender',
            'facebook',
            'telegram',
            'linkedin'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароль не совпадает')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            'photo',
            'phone',
            'gender',
            'facebook',
            'telegram',
            'linkedin'
        ]
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'photo': 'Фото',
            'phone': 'Телефон',
            'gender': 'Пол',
            'facebook': 'facebook',
            'telegram': 'telegram',
            'linkedin': 'linkedin',
        }