from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор модели пользователя. """

    class Meta:
        """ Метаданные сериализатора. """
        model = User
        fields = ('email', 'first_name', 'is_active',)


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор создания пользователя. """

    class Meta:
        """ Метаданные сериализатора. """
        model = User
        fields = ('email', 'first_name', 'last_name', 'password',)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Сериализатор профиля пользователя. """

    class Meta:
        """ Метаданные сериализатора. """
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'full_number',
            'city', 'avatar',
        )
