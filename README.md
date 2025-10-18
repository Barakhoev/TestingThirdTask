# API Testing Project for Petstore

Этот проект содержит автоматизированные тесты для API Petstore (Swagger) с использованием Python и pytest.

## Структура проекта
TestingThirdTask/
├── tests/
│ ├── test_store_requests.py # Тесты для магазина (заказы, инвентарь)
│ └── test_user_requests.py # Тесты для пользователей
├── base_request.py # Базовый класс для работы с API
├── requirements.txt # Зависимости проекта
└── README.md # Документация

## Установка и настройка

1. **Клонируйте репозиторий** или создайте папку проекта
2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt

## Запуск тестов
1. **Запуск всех тестов**
    ```bash
    pytest tests/
2. **Запуск тестов для магазина**
    ```bash
    pytest tests/test_store_requests.py -v
3. **Запуск тестов для пользователей**
    ```bash
    pytest tests/test_user_requests.py -v
4. **Запуск с подробным выводом**
    ```bash
    pytest tests/ -v -s

## Описание тестов
1. **Тесты магазина (Store API)**
test_create_order - создание нового заказа
test_get_order - получение информации о заказе по ID
test_get_inventory - получение инвентаря магазина
test_delete_order - удаление заказа

2. **Тесты пользователей (User API)**
test_create_user - создание нового пользователя
test_get_user - получение информации о пользователе
test_update_user - обновление данных пользователя
test_delete_user - удаление пользователя

## Базовый URL API
Все тесты используют базовый URL: https://petstore.swagger.io/v2

## Классы API
1. **BaseRequest**
    Базовый класс для работы с HTTP-запросами, предоставляет методы:
        get() - GET запрос
        post() - POST запрос
        put() - PUT запрос
        delete() - DELETE запрос

2. **StoreRequests**
    Класс для работы с API магазина, методы:
        create_order() - создание заказа
        get_order() - получение заказа по ID
        delete_order() - удаление заказа
        get_inventory() - получение инвентаря

3. **UserRequests**
    Класс для работы с API пользователей, методы:
        create_user() - создание пользователя
        get_user() - получение пользователя по username
        update_user() - обновление данных пользователя
        delete_user() - удаление пользователя

## Тестовые данные
1. **Для заказов:**
    {
        "id": 1010,
        "petId": 5,
        "quantity": 1,
        "shipDate": "2025-10-17T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

2. **Для пользователей:**
    {
        "id": 9999,
        "username": "pytest_user",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@user.com",
        "password": "12345",
        "phone": "1234567890",
        "userStatus": 1
    }

## Особенности
Автоматическое логирование всех запросов и ответов
Использование фикстур pytest для переиспользования данных
Проверка статус-кодов и структуры ответов
Обработка различных сценариев (успех/не найдено)

## Требования
Python 3.7+
Библиотеки из requirements.txt
Доступ к интернету для работы с Petstore API
