from django.contrib.auth.models import AbstractUser
from django.db import models


class Visit(models.Model):
    count = models.PositiveIntegerField(default=0)  # Общее количество посещений
    count1 = models.PositiveIntegerField(default=0)  # Дополнительное поле count
    count2 = models.PositiveIntegerField(default=0)  # Еще одно поле count
    active_count = models.PositiveIntegerField(default=0)  # Количество активных пользователей
    inactive_count = models.PositiveIntegerField(default=0)  # Количество неактивных пользователей

    def __str__(self):
        return f"Total Visits: {self.count}, Count1: {self.count1}, Count2: {self.count2}, Active Count: {self.active_count}, Inactive Count: {self.inactive_count}"

    class Meta:
        verbose_name = 'Статистика'


    def __str__(self):
        return f"Total Visits: {self.count}, Count1: {self.count1}, Count2: {self.count2}"

    class Meta:
        verbose_name = 'Статистика'


class CustomUser(AbstractUser):
    last_activity = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set", 
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions_set", 
        related_query_name="user",
    )
