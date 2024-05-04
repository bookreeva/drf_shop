from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import LoginForm, ProfileForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    """ Пользователь в административной панели. """

    add_form = LoginForm
    form = ProfileForm
    model = User

    list_display = ("id", "email", "is_staff", "is_active", "full_number",)
    list_filter = ("email", "city", "is_staff", "is_active",)
    list_display_links = ("email",)

    # Поля "Основные" и "Права доступа" в административной панели
    # просмотра деталей пользователя.
    fieldsets = (
        ("Основные", {
            "fields": ("email", "password",)
        }
         ),
        ("Персональные данные", {
            "fields": ("code", "phone", "city", "avatar",)
        }
         ),
        ("Права доступа", {
            "fields": ("is_staff", "is_active", "groups", "user_permissions")
        }
         ),
    )
    # Поля для создания пользователя в административной панели.
    # "Wide" - класс для несворачиваемой панели с полями.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions",
            )
        }
         ),
    )

    search_fields = ("email", "city",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
