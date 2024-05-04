from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from shop.models import Product, SubCategory, Category, CartItem, Cart


# PRODUCT

class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор модели продукта. """
    subcategory = StringRelatedField()
    images = serializers.SerializerMethodField(read_only=True)

    def get_images(self, obj):
        """ Возвращает список изображений. """
        return [
            obj.image_sm.url if obj.image_sm else None,
            obj.image_md.url if obj.image_md else None,
            obj.image_lg.url if obj.image_lg else None,
        ]

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'images', 'price', 'subcategory']


class ShortProductSerializer(serializers.ModelSerializer):
    """ Сериализатор модели продукта (короткий). """

    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


# SUBCATEGORY

class SubCategorySerializer(serializers.ModelSerializer):
    """ Сериализатор модели подкатегории. """
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'slug', 'image', 'category', 'products']


# CATEGORY

class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор модели категории. """
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'image', 'subcategories']


# CARTITEM

class CartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор модели позиции. """
    product = ShortProductSerializer(many=False)
    total = serializers.SerializerMethodField()

    def get_total(self, instance) -> float:
        """ Возвращает произведение стоимости на количество одной позиции. """
        return instance.quantity * instance.product.price

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'total']


class AddCartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор добавления позиции. """

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]


class UpdateCartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор изменения позиции. """

    class Meta:
        model = CartItem
        fields = ["quantity"]


# CART

class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор модели корзины. """
    items = CartItemSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    def get_total_amount(self, instance):
        """ Возвращает общую стоимость всех товаров в корзине. """
        items_all = instance.items.all()
        return sum(item.quantity * item.product.price for item in items_all)

    def get_total_quantity(self, instance):
        """ Возвращает количество товаров в корзине. """
        items_all = instance.items.all()
        return sum(item.quantity for item in items_all)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_amount", "total_quantity"]
