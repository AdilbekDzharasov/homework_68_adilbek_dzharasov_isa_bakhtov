from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class VacancyCategory(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        null=False,
        blank=False,
        max_length=100
    )

    class Meta:
        verbose_name = 'Категория вакансии'
        verbose_name_plural = 'Категории вакансий'

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='vacancies_view',
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False
    )
    salary = models.PositiveIntegerField(
        verbose_name='Зарплата',
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name='Детальное описание',
        null=False,
        blank=False,
    )
    experience_time = models.PositiveIntegerField(
        verbose_name='Опыт работы (лет)',
        null=False,
        blank=False
    )
    is_public = models.BooleanField(
        verbose_name='Опубликовать?',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    vacancy_category = models.ForeignKey(
        to='hh_app.VacancyCategory',
        verbose_name=('Категория вакансии'),
        on_delete=models.CASCADE,
        related_name='vacancies_view'
    )

    def __str__(self):
        return f"{self.author} - {self.name}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Resume(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=get_user_model(),
        related_name='resumes',
        blank=True,
        on_delete=models.CASCADE
    )
    salary_level = models.FloatField(
        verbose_name='Желаемая зарплата',
        null=True,
        blank=False
    )
    info_user = models.TextField(
        verbose_name='Информация о себе',
        max_length=3000,
        null=True,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        null=True,
        blank=False,
    )
    phone = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )
    telegram = models.CharField(
        verbose_name='Telegram',
        max_length=200,
        null=True,
        blank=False
    )
    linkedin = models.CharField(
        verbose_name='Linkedin',
        max_length=200,
        null=True,
        blank=False
    )
    facebook = models.CharField(
        verbose_name='Facebook',
        max_length=200,
        null=True,
        blank=False
    )
    is_public = models.BooleanField(
        verbose_name='Опубликовать?',
        default=False,
        null=False
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'Автор: {self.author}. Email: {self.email}. Желаемая зарплата: {self.salary_level}'

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


class CategoryEducationChoices(TextChoices):
    AVERAGE = 'average', 'Среднее'
    SECONDARY = 'secondary special', 'Среднее специальное'
    HIGHER = 'higher', 'Высшее'
    MAGISTRACY = 'magistracy', 'Магистратура'
    OTHER = 'other', 'Другое'


class Education(models.Model):
    resume = models.ForeignKey(
        to='hh_app.Resume',
        verbose_name='Резюме',
        related_name='education',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    institution_name = models.CharField(
        verbose_name='Название учебного заведения',
        max_length=300,
        null=True,
        blank=False
    )
    speciality = models.CharField(
        verbose_name='Специальность',
        max_length=300,
        null=True,
        blank=False
    )
    category_education = models.CharField(
        verbose_name='Категория образования',
        choices=CategoryEducationChoices.choices,
        max_length=100,
        null=True,
        blank=False,
    )
    begin_date = models.DateField(
        verbose_name='Начало обучения',
        max_length=100,
        null=True,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='Окончание обучения',
        max_length=100,
        null=True,
        blank=False
    )
    faculty = models.CharField(
        verbose_name='Факультет',
        max_length=200,
        null=True,
        blank=False
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.institution_name} {self.speciality} {self.begin_date} {self.end_date} '

    class Meta():
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'


class Experience(models.Model):
    resume = models.ForeignKey(
        to='hh_app.Resume',
        verbose_name='Резюме',
        related_name='experience',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    company = models.CharField(
        verbose_name='Название организации',
        max_length=300,
        null=True,
        blank=False
    )
    begin_date = models.DateField(
        verbose_name='Начало работы',
        max_length=100,
        null=True,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='Окончание работы',
        max_length=100,
        null=True,
        blank=False
    )
    job_title = models.CharField(
        verbose_name='Должность',
        max_length=300,
        null=True,
        blank=False,
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.company}{self.job_title} {self.begin_date} {self.end_date}'

    class Meta():
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Respond(models.Model):
    resume = models.ForeignKey(
        to='hh_app.Resume',
        verbose_name='Резюме',
        related_name='responses',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    vacancy = models.ForeignKey(
        to='hh_app.Vacancy',
        verbose_name='Вакансия',
        on_delete=models.CASCADE,
        related_name='responses',
        null=True,
        blank=False
    )
    author = models.ForeignKey(
        verbose_name='Автор отклика',
        to=get_user_model(),
        related_name='responses',
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Отклик на {self.vacancy}, от автора {self.author}'

    class Meta():
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Message(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='message',
    )
    respond = models.ForeignKey(
        to='hh_app.Respond',
        verbose_name='Отклик',
        on_delete=models.CASCADE,
        related_name='message'
    )
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'{self.author}: {self.respond}'

    class Meta:
        verbose_name = 'Сообщение на отклик'
        verbose_name_plural = 'Сообщения на отклики'

