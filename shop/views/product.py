from rest_framework import viewsets

from shop.models import Product
from shop.paginators import ShopPaginator
from shop.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ Сет представлений для модели продукта. """
    queryset = Product.objects.order_by('title')
    pagination_class = ShopPaginator
    serializer_class = ProductSerializer
    lookup_field = 'slug'
