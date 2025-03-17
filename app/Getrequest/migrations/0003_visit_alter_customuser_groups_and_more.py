# Generated by Django 4.2.7 on 2025-03-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Getrequest', '0002_delete_visit_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('active_count', models.PositiveIntegerField(default=0)),
                ('inactive_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Статистика',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_permissions_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
