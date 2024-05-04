from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.models import CartItem, Cart, Product
from shop.permissions import IsOwner
from shop.serializers import CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    """ Сет представлений для модели позиции. """
    permission_classes = [IsAuthenticated, IsOwner]
    default_serializer = CartItemSerializer
    serializers = {
        'create': AddCartItemSerializer,
        'update': UpdateCartItemSerializer,
    }

    def get_queryset(self):
        """ Возвращает список всех позиций в корзине для текущего пользователя. """
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)

    def get_serializer_class(self):
        """ Возвращает сериализатор в зависимости от запроса. """
        return self.serializers.get(self.action, self.default_serializer)

    def create(self, request, *args, **kwargs):
        """
        Создает или обновляет позицию корзины.
        Если позиция уже существует в корзине - ее количество увеличивается.
        """
        card_id = request.data.get('card_id')
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart = Cart.objects.get(id=card_id, user=request.user)
        product = Product.objects.get(id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            quantity=quantity
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ Обновляет поле количества товаров. """
        cart_item = self.get_object()
        quantity = request.data.get('quantity')

        if quantity:
            cart_item.quantity = quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """ Удаляет позицию товара в корзине. """
        cart_item = self.get_object()
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
