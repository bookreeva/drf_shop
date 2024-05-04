from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Класс тестирования модели пользователя. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='lola@join.com',
            password='123qwe456rty'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_user(self) -> None:
        """ Тестирование регистрации нового пользователя. """

        data = {
            'email': 'testuser@test.com',
            'password': 'testpassword'
        }

        response = self.client.post(
            '/users/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_superuser(self) -> None:
        """ Тестирование создания суперпользователя. """

        self.momo = User.objects.create_superuser(
            email='testuser@test.com',
            password='testpassword'
        )

        self.assertEqual(self.momo.is_superuser, True)

    def test_create_superuser_errors(self) -> None:
        """
        Тестирование создания суперпользователя со статусами
        is_staff, is_superuser - False.
        """

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@test.com',
                password='testpassword',
                is_staff=False
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@test.com',
                password='testpassword',
                is_superuser=False
            )

    def test_create_superuser_without_email(self):  # type: ignore
        """
        Тестирование создания суперпользователя со статусами
        is_staff, is_superuser - False.
        """

        with self.assertRaises(ValueError):
            User.objects.create_superuser(password='testpassword', email=None)

    def test_view_user_list(self) -> None:
        """ Тестирование просмотра списка пользователей. """

        # Просматривать список может только суперпользователь.
        response = self.client.get(
            '/users/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(
            response.json(),
            {
                'detail': 'Вы не являетесь супер пользователем.'
            }
        )

    def test_view_user_detail(self) -> None:
        """ Тестирование просмотра профиля пользователя. """

        response = self.client.get(
            f'/users/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_user(self) -> None:
        """ Тестирование редактирования профиля пользователя. """

        data = {
            'email': 'lola@join.com',
            'city': 'Москва'
        }

        response = self.client.put(
            f'/users/{self.user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self) -> None:
        """ Тестирование удаления профиля пользователя. """

        response = self.client.delete(
            f'/users/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str_method_email(self) -> None:
        """ Тестирование метода str модели пользователя. """

        str_data = f"{self.user.email}"

        self.assertEqual(str(self.user), str_data)

    def test_str_method_name(self) -> None:
        """ Тестирование метода str модели пользователя. """

        self.user.first_name = 'Mimi'
        str_data = f"{self.user.first_name}"

        self.assertEqual(str(self.user), str_data)
