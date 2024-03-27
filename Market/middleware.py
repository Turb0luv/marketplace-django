from datetime import datetime
from .models import UserIPAddress, UserProfile


class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UserProfile.objects.get_or_create(user=request.user)
        response = self.get_response(request)
        return response


class UserIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Сохраняем IP-адрес пользователя
        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            UserIPAddress.objects.get_or_create(user=request.user,
                                         ip_address=ip_address)

        response = self.get_response(request)
        return response
