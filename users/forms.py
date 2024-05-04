from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class LoginForm(UserCreationForm):
    """ Форма создания пользователя. """

    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(UserChangeForm):
    """ Форма редактирования пользователя. """

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'city',
            'avatar', 'is_active', 'code', 'phone',
        )
