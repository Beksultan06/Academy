from django.contrib import admin
from .models import *
# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Фотография', {
            'fields': ['photo', 'date'],
        }),
        )
admin.site.register(Photos, PhotosAdmin)