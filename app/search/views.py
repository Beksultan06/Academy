from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from app.students.models import ScientificJournal
from app.ology.models import Ology
from app.AboutAcademy.models import About
from app.education.models import AllEducation
from app.applicants.models import Academic
from app.mainpage.models import Settings
from app.management.models import *
from app.activity.models import Activity
from app.AboutAcademy.models import About
from app.students.serializers import ScientificJournalSerializer
from app.ology.serializers import OlogySerializer
from app.AboutAcademy.serializers import AboutSerializer
from app.education.serializers import AllEducationSerializer
from app.applicants.serializers import AcademicSerializer
from app.mainpage.serializers import SettingsSerializers
from app.activity.serializers import ActivityCardSerializer
from app.AboutAcademy.serializers import AboutSerializer
from .filters import *
from app.students.translation import *
from app.ology.translation import * 
from app.AboutAcademy.translation import *
from app.education.translation import *
from app.applicants.translation import *
from app.mainpage.translation import *
from app.management.translation import *
from app.activity.translations import *


from django.conf import settings
from django.utils.translation import get_language

class GlobalSearchView(APIView):
    def get(self, request):
        query = request.query_params.get("title", "")

        if not query:
            return Response({"results": []}) 

        results = []
        current_language = get_language()  


        models = [
            (ScientificJournal, ScientificJournalSerializer, ["title"]),
            (Ology, OlogySerializer, ["title"]),
            #(About, AboutSerializer, ["title"]),
            (Settings, SettingsSerializers, [
                "title_banner", "title_news", "title_scientific_degrees", 
                "title_additional_professional_education", "title_courses", 
                "title_we_suggest_you_watch_it", "title_journal_of_the_islamic_academy",
                "title_journals_of_partner_universities", "title_gallery", "title_obj"
            ]),
            (AllEducation, AllEducationSerializer, ["title"]),
            (Academic, AcademicSerializer, ["title"]),
            (Activity, ActivityCardSerializer, ["title", "title_obj"]),
            (About, AboutSerializer, [f"title_main_{current_language}", f"title2_{current_language}", f"title_page_{current_language}"]),
        ]

        for model, serializer, fields in models:
            q_objects = Q()
            for field in fields:
                # Используем поля с учетом текущего языка
                q_objects |= Q(**{f"{field}__icontains": query})

            matches = model.objects.filter(q_objects)
            results.extend(serializer(matches, many=True).data)

        return Response({"results": results})

