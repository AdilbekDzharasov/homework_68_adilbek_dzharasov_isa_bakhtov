# Generated by Django 4.1.3 on 2022-11-19 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hh_app', '0002_vacancycategory_vacancy_vacancy_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_level', models.FloatField(null=True, verbose_name='Желаемая зарплата')),
                ('info_user', models.TextField(max_length=3000, null=True, verbose_name='Информация о себе')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Номер телефона')),
                ('telegram', models.CharField(max_length=200, null=True, verbose_name='Telegram')),
                ('linkedin', models.CharField(max_length=200, null=True, verbose_name='Linkedin')),
                ('facebook', models.CharField(max_length=200, null=True, verbose_name='Facebook')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовать?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL, verbose_name='Автор резюме')),
            ],
        ),
    ]
