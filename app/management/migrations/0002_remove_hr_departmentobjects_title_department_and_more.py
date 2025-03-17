# Generated by Django 4.2.7 on 2025-03-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department',
        ),
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department_ar',
        ),
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department_en',
        ),
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department_ky',
        ),
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department_ru',
        ),
        migrations.RemoveField(
            model_name='hr_departmentobjects',
            name='title_department_tr',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title_ar',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title_ky',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='rectorobjectstitle',
            name='title_tr',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works_ar',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works_en',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works_ky',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works_ru',
        ),
        migrations.RemoveField(
            model_name='scientworksrectorobjects',
            name='title_works_tr',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy_ar',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy_en',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy_ky',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy_ru',
        ),
        migrations.RemoveField(
            model_name='vacanciesobjects',
            name='title_vacancy_tr',
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department_ar',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department_en',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department_ky',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department_ru',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='hr_departmentobjects',
            name='title2_department_tr',
            field=models.CharField(blank=True, default='Объект для вакансии', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2',
            field=models.CharField(default='Под заголовок объекта', max_length=255, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2_ar',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2_en',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2_ky',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2_ru',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='rectorobjectstitle',
            name='title2_tr',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works',
            field=models.CharField(default='Под заголовок объекта', max_length=255, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works_ar',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works_en',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works_ky',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works_ru',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='scientworksrectorobjects',
            name='title2_works_tr',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy',
            field=models.CharField(default='Под заголовок объекта', max_length=255, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy_ar',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy_en',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy_ky',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy_ru',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
        migrations.AddField(
            model_name='vacanciesobjects',
            name='title2_vacancy_tr',
            field=models.CharField(default='Под заголовок объекта', max_length=255, null=True, verbose_name='Под заголовок объекта'),
        ),
    ]
