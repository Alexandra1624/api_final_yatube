# Проект «API для Yatube»
API для работы с Yatube.    
Функционал: Авторизация по JWT токену.      
Сериализация данных для всех моделей проекта (Post, Comment, Group, Follow)     
Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:         
git clone https://github.com/Alexandra1624/api_final_yatube.git     
cd api_final_yatube       
    
Cоздать и активировать виртуальное окружение:     
python -m venv venv     
source venv/Scripts/activate    
    
Обновить pip и установить зависимости из файла requirements.txt:    
python -m pip install --upgrade pip       
pip install -r requirements.txt     
        
Выполнить миграции:     
cd yatube_api   
python manage.py migrate   
    
Создать суперпользователя:      
python manage.py createsuperuser
        
Проверка тестов:      
pytest
        
Запустить проект:     
python manage.py runserver
      
Сервер запущен на странице:     
http://localhost:8000

Спецификация и эндпоинты доступны в документации:       
http://localhost:8000/redoc/
## Примеры запросов к API
Для доступа к API необходимо получить токен:    
Нужно выполнить POST-запрос http://127.0.0.1:8000/api/v1/jwt/create/, передав поля username и password. API вернет JWT-токен.

Дальше, передав токен можно будет обращаться к методам, например:

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

Выберите тип авторизации Bearer Token во вкладке Authorization и укажите JWT-токен там.
    
### GET /api/v1/posts/
    Получаем список всех публикаций:
    [
    {
        "id": 1,
        "text": "Текст1",
        "author": "admin",
        "image": null,
        "group": null,
        "pub_date": "2022-04-01T07:54:38.032822Z"
    }
    ]
     
### POST /api/v1/posts/
    Водим обязательное поле "text":
    {
    "text": "stringstring"
    }
   
                  
    Записываем новый пост.
    {
    "id": 3,
    "text": "stringstring",
    "author": "admin",
    "image": null,
    "group": null,
    "pub_date": "2022-04-01T08:10:59.562063Z"
    }
        
### GET /api/v1/posts/2
    Получаем пост номер 2:
    {
    "id": 2,
    "text": "stringstring",
    "author": "admin",
    "image": null,
    "group": null,
    "pub_date": "2022-04-01T08:07:08.608145Z"
     }
