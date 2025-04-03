from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.activity.models import Activity
from app.activity.serializers import ActivityCardSerializer
from collections import defaultdict

class ActivityViewSet(ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        grouped = defaultdict(list)

        for activity in activities:
            serializer = ActivityCardSerializer(activity, context={'request': request})
            grouped[activity.link].append(serializer.data)

        nav_elements = []
        for i, (link, cards) in enumerate(grouped.items(), start=1):
            nav_elements.append({
                "id": i,
                "link": link,
                "cards": cards
            })

        response = {
            "activity": {
                "page": "Деятельность",
                "banner": {
                    "title": "Наследие Успеха Наши Достижения",
                    "description": "Исламская Академия гордится тем, что предоставляет своим студентам уникальные возможности для роста и развития. Мы стремимся не только к передаче знаний, но и к формированию личностей, готовых внести вклад в общество."
                },
                "navElements": nav_elements
            }
        }
        return Response(response)
