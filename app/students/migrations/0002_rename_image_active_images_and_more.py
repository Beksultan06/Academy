# Generated by Django 4.2.7 on 2025-03-01 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='active',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='parliament',
            old_name='image',
            new_name='images',
        ),
    ]
