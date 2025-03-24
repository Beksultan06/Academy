
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.yasg import urlpatterns_yasg

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('api/v1/AboutAcademy/',include('app.AboutAcademy.urls')),
    path('api/v1/gellary',include('app.gellary.urls')),
    path('api/v1/ology/', include('app.ology.urls')),
    path('api/v1/education/', include('app.education.urls')),
    path("api/v1/management/", include("app.management.urls")),
    path("api/v1/applicants/", include("app.applicants.urls")),
    path("api/v1/main/", include("app.mainpage.urls")),
    path("api/v1/activity/", include("app.activity.urls")),
    path("api/vi/Getrequest/", include("app.Getrequest.urls")),
    path("api/v1/students/", include("app.students.urls")),
    path("", include(urlpatterns_yasg)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)