from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение категорий в административной панели. """
    list_display = ('id', 'title', 'slug', 'get_image',)
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        """ Возвращает содержимое значения поля image. """
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    get_image.short_description = 'Изображение'


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """ Отображение подкатегорий в административной панели. """
    list_display = ('id', 'title', 'slug', 'get_image', 'category')
    list_display_links = ['title']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        """ Возвращает содержимое значения поля image. """
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    get_image.short_description = 'Изображение'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Отображение продуктов в административной панели. """
    list_display = ('id', 'title', 'slug', 'price', 'subcategory', 'get_image_md')
    list_display_links = ['title']
    list_filter = ('subcategory',)
    prepopulated_fields = {'slug': ('title',)}

    def get_image_md(self, obj):
        """ Возвращает содержимое значения поля image_md. """
        if obj.image_md:
            return mark_safe("<img src='{}' width='60' />".format(obj.image_md.url))
        return "None"

    get_image_md.short_description = 'Изображение (среднее)'
