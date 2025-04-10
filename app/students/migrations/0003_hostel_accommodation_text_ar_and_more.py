# Generated by Django 4.2.7 on 2025-03-12 12:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_image_active_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='accommodation_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='accommodation_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для условий проживания'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание страницы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='reviews_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='security_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для безопасности и порядка'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='spiritual_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовной атмосферы'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для студенческого быта'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='student_life_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для студенческого быта'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='cultural_events_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для культурных и общественных мероприятий'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='education_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для образования и науки'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='reviews_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для отзывов студентов'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='spiritual_development_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для духовного развития'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_text_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_text_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_text_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='sports_title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок для спорта и здорового образа жизни'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='title_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='title_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='title_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='title_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='studentlife',
            name='title_tr',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Заголовок страницы'),
        ),
    ]
