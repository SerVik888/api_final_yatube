# Проект на Django «API для Yatube»

## Краткое описание проекта.

Через api возможно получение и изменение постов и комментариев.\
Получение групп(другие действия доступны только через админку).\
Получение и поиск по подпискам(только для авторизованных пользователей).\
Работа с пользователями реалирована при помощи *djoser*.\
Реализована аутентификация по по JWT-токену при помощи *djangorestframework-simplejwt* для обеспечения безопасности API.\
Тесты написаны на *pytest*

### При запуске проекта буду достнупны такие эндпоинты:

- api/v1/users/ - адрес для работы с пользоваетлями\
`GET`, `POST`, `PUT`, `DELETE` Нужна авторизация

- api/v1/follow/ - адрес для работы с подписками\
`GET`, `POST` Нужна авторизация

- api/v1/groups/ - адрес для работы с группами\
`GET`, Нужна авторизация

- api/v1/posts/ - адрес для работы с постами\
`GET`, Не нужна авторизация\
`POST`, `PUT`, `DELETE` Нужна авторизация

- api/v1/posts/{post_id}/comments/ - адрес для работы с комментариями\
`GET`, Не нужна авторизация\
`POST`, `PUT`, `DELETE` Нужна авторизация

- api/v1/jwt/create/ - адрес для работы с токенами\
`POST`, Не нужна авторизация

*Более подробное описание будет доступно в документации по адресу http://127.0.0.1:8000/redoc/ 
после запуска проекта.*

### Как запустить проект:

`git clone git@github.com:SerVik888/api_final_yatube.git` -> клонировать репозиторий

`cd api_final_yatube` -> перейти в репозиторий

* Если у вас Linux/macOS\
    `python3 -m venv env` -> создать виртуальное окружение\
    `source env/bin/activate` -> активировать виртуальное окружение\
    `python3 -m pip install --upgrade pip` -> обновить установщик\
    `pip install -r requirements.txt` -> установить зависимости из файла requirements.txt\
    `python3 manage.py migrate` -> выполнить миграции\
    `python3 manage.py createsuperuser` -> создать суперпользователя\
    `python3 manage.py runserver` -> запустить проект

* Если у вас windows\
    `python -m venv env` -> создать виртуальное окружение\
    `source venv/Scripts/activate` -> активировать виртуальное окружение\
    `python -m pip install --upgrade pip` -> обновить установщик\
    `pip install -r requirements.txt` -> установить зависимости из файла requirements.txt\
    `python manage.py migrate` -> выполнить миграции\
    `python manage.py createsuperuser` -> создать суперпользователя\
    `python manage.py runserver` -> запустить проект

### Cписок используемых технологий

- Django
- pytest
- djangorestframework
- djangorestframework-simplejwt
- djoser


Автор: Сафонов Сергей
Почта: [sergey_safonov86@inbox.ru](mailto:sergey_safonov86@inbox.ru)