# CARS-API
### RESTful API для сбора и фильтрации данных об автомобилях

Использован Django Rest Framework, БД - SQLite;

Для защиты API реализованы аутентификация и авторизация (Session-based + Token-based), API и документация доступны только зарегистрированным пользователям;

Присутствует возможность возможность обновления и удаления автомобилей;

Реализована кастомная пагинация для списка автомобилей(количество объектов на странице по усолчания - 3, для изменения - добавить к адресу ?page_size=число);

Документация к API доступна по адресу http://127.0.0.1:8000/swagger/

## Запуск проекта
- Рядом с файлом .env.example разместить .env файл. Env переменные:
```
SECRET_KEY='some_secret_key'
```
- В основной папке установить и активировать виртуальное окружение
```console  
python -m venv venv
```
```console  
.\venv\Scripts\activate.bat
```

- Установить используемые библиотеки из файла requirements.txt
```console  
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполнить команду для миграций:
```console  
python manage.py migrate
```
- В папке с файлом manage.py создать суперпользователя:
```console  
python manage.py createsuperuser
```
- В папке с файлом manage.py выполнить команду для запуска локального сервера:
```console  
python manage.py runserver
```

- Добавление автомобиля:

POST
```
/api/cars/
```

Response:
```
{ "brand": "Toyota", "model": "Camry", "year": 2020, "fuel_type": "бензин", "transmission": "автоматическая", "mileage": 50000, "price": 25000 }
```
- Получение списка автомобилей по фильтрам:

GET 
```
/api/cars/?brand=Toyota&model=Camry&year=2020&fuel_type=бензин&transmission=автоматическая&mileage_min=40000&mileage_max=60000&price_min=20000&price_max=30000
```
- Получение деталей конкретного автомобиля по ID:

GET 
```
/api/cars/1/
```
