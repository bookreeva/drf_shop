from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.models import Cart
from shop.permissions import IsOwnerItems
from shop.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    """ Сет представлений для модели корзины. """
    permission_classes = [IsAuthenticated, IsOwnerItems]
    serializer_class = CartSerializer

    def get_queryset(self):
        """ Возвращает данные для текущего пользователя. """
        return Cart.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """ Очищает корзину. """
        instance = self.get_object()
        instance.items.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
