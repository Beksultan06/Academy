from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Visit
from django.utils import timezone
from django.contrib.auth import get_user_model
from .serializers import VisitSerializer

User = get_user_model()

class VisitView(APIView):
    def get(self, request):
        visit, created = Visit.objects.get_or_create(id=1)
        
        # Увеличиваем все три поля
        visit.count += 1
        visit.count1 += 1
        visit.count2 += 1

        user = request.user
        if user.is_authenticated:
            user.last_activity = timezone.now()
            user.save()

            active_threshold = timezone.now() - timezone.timedelta(minutes=10)
            if user.last_activity > active_threshold:
                # Увеличиваем активных пользователей
                visit.active_count += 1
            else:
                # Увеличиваем неактивных пользователей
                visit.inactive_count += 1
        else:
            # Увеличиваем количество неактивных пользователей, если пользователь не авторизован
            visit.inactive_count += 1

        visit.save()
        
        # Сериализация данных и отправка ответа
        serializer = VisitSerializer(visit)
        return Response(serializer.data)
