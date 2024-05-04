from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.apps import ShopConfig
from shop.views.cart import CartViewSet
from shop.views.cartitem import CartItemViewSet
from shop.views.category import CategoryViewSet
from shop.views.product import ProductViewSet
from shop.views.subcategory import SubCategoryViewSet

app_name = ShopConfig.name

router = DefaultRouter()
router.register('carts', CartViewSet, basename='cart')
router.register('cart-items', CartItemViewSet, basename='cart-item')
router.register('categories', CategoryViewSet, basename='category')

category_router = DefaultRouter()
category_router.register('', SubCategoryViewSet, basename='subcategory')

subcategory_router = DefaultRouter()
subcategory_router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/', include(subcategory_router.urls)),
    path('api/categories/<slug:category_slug>/', include(category_router.urls)),
    path('api/categories/<slug:category_slug>/<slug:subcategory_slug>/', include(subcategory_router.urls)),
]
