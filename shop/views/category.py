from rest_framework import viewsets

from shop.models import Category
from shop.paginators import ShopPaginator
from shop.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ Сет представлений для модели категории. """
    queryset = Category.objects.order_by('title')
    pagination_class = ShopPaginator
    serializer_class = CategorySerializer
    lookup_field = 'slug'
