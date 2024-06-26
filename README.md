<a id="toup"></a>
<h1>DRF Online-Shop</h1>
<h2>Добро пожаловать! 
Данный DRF-проект представляет собой API магазина, 
использующий авторизацию по электронной почте.</h2>
<h3>Перед началом использования программы создайте файл .env и заполните его данными из файл .env.sample:</h3>


| Шаблон .env.sample |
|--------------------|

```text 
DJANGO_SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

LANGUAGE_CODE=
 ```

<h4>✔️ Создайте виртуальное окружение и активируйте его</h3>
<h4>✔️ Установите зависимости из файла requirements.txt </h3>

<h4>✔️ Далее выполните следующие команды: </h4>

| Описание                                        | Команды                                |
|-------------------------------------------------|----------------------------------------|
| Создать БД в POSTGRESQL                         | ```psql -U postgres```                 |
| Применить миграции                              | ```python manage.py migrate```         |
| Создать суперпользователя для доступа в админку | ```python manage.py createsuperuser``` |


 <div style="display: flex; align-items: center;">
    <div style="display: inline-block; margin: 2px;" >


</div>
  </div>

<h2>Ошибки и улучшения</h2>
Если вы обнаружили ошибки, у вас есть предложения по улучшению данного проекта 
или у вас есть вопросы по использованию API, пожалуйста, присылайте pull request.

[Вверх](#toup)

```commandline

```