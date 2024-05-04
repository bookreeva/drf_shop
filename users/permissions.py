from django.http import HttpRequest
from django.views import View
from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    """ Права доступа для владельца. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request: HttpRequest, view: View, obj: User) -> bool:
        """ Настраивает способ проверки разрешений. """
        return request.user == obj


class IsSuperUser(BasePermission):
    """ Права доступа для супер пользователя. """
    message = 'Вы не являетесь супер пользователем.'

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        """ Настраивает способ проверки разрешений. """
        return request.user.is_superuser
