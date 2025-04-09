from django.urls import path, include
from django.urls import path
from app.AboutAcademy.views import AboutGroupedView

urlpatterns = [
    path('AboutAcademy/', AboutGroupedView.as_view(), name='about-grouped'),
]
