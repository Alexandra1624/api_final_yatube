# Проект «API для Yatube»
## Описание
API для работы с **_Yatube_**.          
**Функционал**: Авторизация по **JWT токену**.      
Сериализация данных для всех моделей проекта (**Post, Comment, Group, Follow**)     
Обработка **GET, POST, PATCH, PUT** и **DELETE** запросов к базе данных проекта **_Yatube_**

## Технологии
- Python 3.7.9
- Django 2.2.16
- Django Rest Framework 3.12.4
- DjangorestFramework-Simplejwt 4.7.2

## Установка:
1. **Клонировать репозиторий и перейти в него в командной строке:**
```sh
git clone https://github.com/Alexandra1624/api_final_yatube.git
cd api_final_yatube
```
2. **Cоздать и активировать виртуальное окружение:**
```sh
python -m venv venv
source venv/Scripts/activate
```

3. **Обновить pip и установить зависимости из файла requirements.txt:**
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. **Выполнить миграции:**
```sh
cd yatube_api
python manage.py migrate
```

5. **Создать суперпользователя:**
```sh
python manage.py createsuperuser
```

6. **Проверка тестов:**
```sh
pytest
```

7. **Запустить проект:**
```sh
python manage.py runserver
```
Сервер запущен на странице:     
http://localhost:8000       
Спецификация и эндпоинты доступны в документации:       
http://localhost:8000/redoc/

## Примеры запросов к API
Для доступа к API необходимо получить ***токен***:      
Нужно выполнить **POST-запрос** http://127.0.0.1:8000/api/v1/jwt/create/, передав поля ***username*** и ***password***. API вернет ***JWT-токен***.

Дальше, передав токен можно будет обращаться к методам, например:
```sh
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)
```
Выберите тип авторизации ***Bearer Token*** во вкладке ***Authorization*** и укажите ***JWT-токен*** там.
```sh
GET /api/v1/posts/
```
Получаем список всех публикаций:

>[
{
    "id": 1,
    "text": "Текст1",
    "author": "admin",
    "image": null,
    "group": null,
    "pub_date": "2022-04-01T07:54:38.032822Z"
}
]

```sh
POST /api/v1/posts/
```
Вводим обязательное поле **"text"**:
>{
"text": "stringstring"
}

Записываем новый пост.
>{
"id": 3,
"text": "stringstring",
"author": "admin",
"image": null,
"group": null,
"pub_date": "2022-04-01T08:10:59.562063Z"
}
```sh
GET /api/v1/posts/2
```
Получаем пост номер 2:
>{
"id": 2,
"text": "stringstring",
"author": "admin",
"image": null,
"group": null,
"pub_date": "2022-04-01T08:07:08.608145Z"
 }
 ## Автор

**_Александра Радионова_**      
https://github.com/Alexandra1624    
https://t.me/alexandra_R1624    
sashamain@yandex.ru
