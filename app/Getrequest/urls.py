from django.urls import path
from .views import VisitView

urlpatterns = [
    path('', VisitView.as_view()),
]