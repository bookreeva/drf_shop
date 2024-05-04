from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """ Модель категории. """
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Slug'
    )
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение категории',
        **NULLABLE
    )

    def __str__(self):
        """ Строковое представление модели категории. """
        return f"{self.title}"

    class Meta:
        """ Метаданные модели категории. """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    """ Модель подкатегории. """
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название подкатегории'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Slug'
    )
    image = models.ImageField(
        upload_to='subcategories/',
        verbose_name='Изображение подкатегории',
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Категория'
    )

    def __str__(self):
        """ Строковое представление модели подкатегории. """
        return f"{self.title} -- {self.category}"

    class Meta:
        """ Метаданные модели подкатегории. """
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """ Модель продукта. """
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    image_sm = models.ImageField(
        upload_to='products/small/',
        verbose_name='Изображение (маленькое)',
        **NULLABLE
    )
    image_md = models.ImageField(
        upload_to='products/medium/',
        verbose_name='Изображение (среднее)',
        **NULLABLE
    )
    image_lg = models.ImageField(
        upload_to='products/large/',
        verbose_name='Изображение (большое)',
        **NULLABLE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Подкатегория'
    )

    def __str__(self):
        """ Строковое представление модели продукта. """
        return f"{self.title} -- {self.subcategory}"

    class Meta:
        """ Метаданные модели продукта. """
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    """ Модель корзины. """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Строковое представление модели корзины. """
        return f"Корзина №{self.pk} для {self.user}"

    class Meta:
        """ Метаданные модели корзины. """
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    """ Модель позиции в корзине. """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='корзина'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Продукт',
    )
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        """ Строковое представление модели позиции в корзине. """
        return f"{self.quantity} х {self.product}"

    class Meta:
        """ Метаданные модели позиции в корзине. """
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'
