# Generated by Django 4.2.7 on 2025-03-13 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Getrequest', '0003_visit_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='active_count',
            new_name='count1',
        ),
        migrations.RenameField(
            model_name='visit',
            old_name='inactive_count',
            new_name='count2',
        ),
    ]
