from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Права доступа для доступа к корзине. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request, view, obj) -> bool:
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.cart.user


class IsOwnerItems(BasePermission):
    """ Права доступа для доступа к текущей позиции в корзине. """
    message = 'Вы не являетесь владельцем страницы.'

    def has_object_permission(self, request, view, obj) -> bool:
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.user
