from django.utils.timezone import now
from .models import Visit
import threading
import time

ACTIVE_USERS = {}

class VisitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_inactive_checker()  # Запускаем проверку на неактивных пользователей

    def __call__(self, request):
        visit, _ = Visit.objects.get_or_create(id=1)
        user_ip = self.get_client_ip(request)

        ACTIVE_USERS[user_ip] = now().timestamp()

        # Обновляем все три счетчика
        visit.count += 1
        visit.count1 += 1
        visit.count2 += 1
        visit.save()

        response = self.get_response(request)
        return response

    def start_inactive_checker(self):
        def reset_inactive_users():
            while True:
                time.sleep(15)  # Периодичность проверки
                current_time = now().timestamp()
                inactive_users = [ip for ip, last_time in ACTIVE_USERS.items() if current_time - last_time > 15]

                # Удаляем неактивных пользователей
                for ip in inactive_users:
                    del ACTIVE_USERS[ip]

                # Обновляем в БД количество активных пользователей
                Visit.objects.filter(id=1).update(count1=len(ACTIVE_USERS), count2=len(ACTIVE_USERS))

        # Запускаем этот процесс в отдельном потоке
        thread = threading.Thread(target=reset_inactive_users, daemon=True)
        thread.start()

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
