# Управление Денежными Потоками

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/b0e4f902-a82a-41ab-89fb-6be1b1db32b7" />
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/1566a79f-b206-48e2-bdc4-e5a92199d829" />
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/0dba7e7f-3d8a-4af9-a9bd-0b058bb58c0a" />
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/6b8c19a8-b2c9-4107-95b4-d002f1cfadef" />

**Управление Денежными Потоками** — это веб-приложение на Django, предназначенное для помощи пользователям в отслеживании доходов и расходов. Оно предоставляет структурированный способ записи финансовых транзакций, их категоризации и фильтрации для анализа. Приложение использует динамические формы для улучшенного пользовательского опыта.

## Возможности

*   **Отслеживание Денежных Потоков**: Регистрация финансовых операций с деталями: дата, сумма, статус, тип, категория, подкатегория и комментарии.
*   **Операции CRUD**: Полный функционал создания, чтения, обновления и удаления для:
    *   Записей денежных потоков
    *   Статусов (например, Оплачено, В ожидании)
    *   Типов (например, Доход, Расход)
    *   Категорий (например, Зарплата, Продукты)
    *   Подкатегорий (например, Бонус, Овощи)
*   **Фильтрация**: Фильтрация записей по диапазону дат, статусу, типу, категории и подкатегории.
*   **Динамические Зависимые Выпадающие Списки**: Выпадающие списки категорий и подкатегорий обновляются на основе выбранного типа и категории с использованием AJAX.
*   **Управление Словарями**: Отдельный раздел для управления статусами, типами, категориями и подкатегориями.
*   **Удобный Интерфейс**: Используются Django формы и шаблоны для ввода и отображения данных.

## Используемые Технологии

*   **Бэкенд**: Python, Django  
*   **Фронтенд**: HTML, CSS (через Django Templates), JavaScript (для AJAX)  
*   **База данных**: SQLite (по умолчанию, настраивается в настройках Django)  
*   **Переменные Окружения**: `python-dotenv`

## Предварительные Требования

Перед началом убедитесь, что у вас установлены:
*   Python (рекомендуется версия 3.8 или выше)
*   pip (менеджер пакетов Python)
*   Git (для клонирования репозитория)

## Установка и Настройка

Следуйте этим шагам, чтобы развернуть проект на локальной машине.

1.  **Клонируйте Репозиторий**
    ```bash
    git clone https://github.com/javoxirone/cash-flow-management.git
    cd cash-flow-management
    ```

2.  **Создайте и Активируйте Виртуальное Окружение**
    *   Для Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   Для Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Установите Зависимости**
    Создайте файл `requirements.txt` в корне проекта со следующим содержимым:
    ```txt
    Django>=5.0,<6.0
    python-dotenv
    # Добавьте другие зависимости при необходимости
    ```
    Затем установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
    *(Примечание: Хорошей практикой является генерация `requirements.txt` из рабочей среды с помощью `pip freeze > requirements.txt`)*

4.  **Настройте Переменные Окружения**
    Создайте файл `.env` в корне проекта (там, где находится `manage.py`):
    ```bash
    touch .env
    ```
    Откройте `.env` и добавьте ваш `SECRET_KEY` Django:
    ```env
    SECRET_KEY='ваш_уникальный_секретный_ключ'
    ```
    Замените `'ваш_уникальный_секретный_ключ'` на сильный уникальный ключ. Его можно сгенерировать с помощью онлайн-сервиса или скрипта на Python.

5.  **Примените Миграции Базы Данных**
    Это создаст необходимые таблицы в базе данных на основе моделей из `main/models.py`.
    ```bash
    python manage.py migrate
    ```

## Запуск Проекта

1.  **Запустите Сервер Разработки**
    ```bash
    python manage.py runserver
    ```

2.  **Откройте Приложение**
    В браузере перейдите по адресу:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Вы увидите главную страницу со списком записей (если они есть).

## Использование

Приложение содержит несколько ключевых разделов:

*   **Главная Страница (`/`)**:
    *   Список всех записей.
    *   Форма фильтрации по дате, статусу, типу, категории и подкатегории.
    *   Ссылка для создания новой записи.
    *   Возможность редактировать или удалить записи.

*   **Создание Записи (`/cash-flow/create/`)**:
    *   Форма добавления новой транзакции.
    *   Поля Категория и Подкатегория обновляются в зависимости от выбранного Типа и Категории.

*   **Редактирование Записи (`/cash-flow/<id>/update/`)**:
    *   Редактирование существующей записи.

*   **Словари (`/dictionaries/`)**:
    *   Просмотр и управление списками Статусов, Типов, Категорий и Подкатегорий.
    *   Ссылки на создание, редактирование и удаление:
    *   **Управление Статусами**:
        *   Создание: `/dictionaries/status/create/`
        *   Редактирование: `/dictionaries/status/<id>/update/`
        *   Удаление: `/dictionaries/status/<id>/delete/`
    *   **Управление Типами**:
        *   Создание: `/dictionaries/type/create/`
        *   Редактирование: `/dictionaries/type/<id>/update/`
        *   Удаление: `/dictionaries/type/<id>/delete/`
    *   **Управление Категориями**:
        *   Создание: `/dictionaries/category/create/`
        *   Редактирование: `/dictionaries/category/<id>/update/`
        *   Удаление: `/dictionaries/category/<id>/delete/`
    *   **Управление Подкатегориями**:
        *   Создание: `/dictionaries/subcategory/create/`
        *   Редактирование: `/dictionaries/subcategory/<id>/update/`
        *   Удаление: `/dictionaries/subcategory/<id>/delete/`

## Структура Проекта

*   `project/`: Содержит основные конфигурационные файлы Django (`settings.py`, `urls.py`, `wsgi.py`)
*   `main/`: Django-приложение с основной логикой:
    *   `models.py`: Модели (CashFlow, Status, Type, Category, Subcategory)
    *   `views.py`: Обработка запросов и формирование ответов
    *   `forms.py`: Формы для ввода и валидации данных
    *   `urls.py`: URL-маршруты для приложения `main`
    *   `templates/main/`: (Предполагается) HTML-шаблоны приложения `main`
*   `templates/`: (Предполагается в корне проекта) Глобальная папка шаблонов
*   `manage.py`: Утилита Django для административных задач
*   `.env`: Файл с переменными окружения (например, `SECRET_KEY`) — необходимо создать вручную
*   `db.sqlite3`: Файл базы данных SQLite (создается после миграций)
