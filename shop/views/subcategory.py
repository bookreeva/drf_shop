from rest_framework import viewsets

from shop.models import SubCategory
from shop.serializers import SubCategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """ Сет преставлений для модели подкатегории. """
    queryset = SubCategory.objects.order_by('title')
    serializer_class = SubCategorySerializer
    lookup_field = 'slug'
