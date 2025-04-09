import django_filters
from django_filters import rest_framework as filters
from app.students.models import ScientificJournal
from app.ology.models import *
from app.AboutAcademy.models import *
from app.education.models import *
from app.applicants.models import *
from app.mainpage.models import *
from app.management.models import *
from app.activity.models import *


class ScientificJournalFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = ScientificJournal
        fields = ["title"]

class OlogyFilter(filters.FilterSet): 
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Ology
        fields = ["title"]

class LeadershipFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Leadership
        fields = ["title"]

class SettingsFilter(filters.FilterSet):
    title_banner = filters.CharFilter(field_name='title_banner', lookup_expr='icontains')
    title_news = filters.CharFilter(field_name='title_news', lookup_expr='icontains')
    title_scientific_degrees = filters.CharFilter(field_name='title_scientific_degrees', lookup_expr='icontains')
    title_additional_professional_education = filters.CharFilter(field_name='title_additional_professional_education', lookup_expr='icontains')
    title_courses = filters.CharFilter(field_name='title_courses', lookup_expr='icontains')
    title_we_suggest_you_watch_it = filters.CharFilter(field_name='title_we_suggest_you_watch_it', lookup_expr='icontains')
    title_journal_of_the_islamic_academy = filters.CharFilter(field_name='title_journal_of_the_islamic_academy', lookup_expr='icontains')
    title_journals_of_partner_universities = filters.CharFilter(field_name='title_journals_of_partner_universities', lookup_expr='icontains')
    title_gallery = filters.CharFilter(field_name='title_gallery', lookup_expr='icontains')
    title_obj = filters.CharFilter(field_name='title_obj', lookup_expr='icontains')

    class Meta:
        model = Settings
        fields = [
            "title_banner", "title_news", "title_scientific_degrees", "title_additional_professional_education",
            "title_courses", "title_we_suggest_you_watch_it", "title_journal_of_the_islamic_academy",
            "title_journals_of_partner_universities", "title_gallery", "title_obj"
        ]

class AllEducationFilter(filters.Filter):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = AllEducation
        fields = ["title"]

class AcademicFilter(filters.Filter):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Academic
        fields = ["title"]

class ActivityFilter(filters.Filter):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    title_obj = filters.CharFilter(field_name='title_obj', lookup_expr='icontains')

    class Meta:
        model = Activity
        fields = ["title", "title_obj"]

class AboutFilter(filters.Filter):
    title_main = filters.CharFilter(field_name='title', lookup_expr='icontains')
    title2 = filters.CharFilter(field_name='title2', lookup_expr='icontains')
    title_page = filters.CharFilter(field_name='title_page', lookup_expr='icontains')

