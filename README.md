# Проект Mobius — «Сервис прогнозирования спроса на товары»

### Описание:
Сервис, предназначенный для прогнозирования спроса на товары на ближайшие 14 дней, 
и позволяющий просматривать Пользователю необходимую статистику, а также выгружать ее 
в excel-файле.

### Используемые технологии
- Django
- Django Rest Framework
- Docker
- Docker-compose
- Gunicorn
- Nginx
- PostgreSQL

### Workflow
- **tests:** Проверка кода на соответствие PEP8.
- **push Docker image to Docker Hub:** Сборка и публикация образа на DockerHub.
- **deploy:** Автоматический деплой на боевой сервер при пуше в главную ветку main.
- **send_massage:** Отправка уведомления в телеграм-чат.

### Подготовка и запуск проекта
- Выполнить вход на удаленный сервер
- Установить docker на сервер:
```bash
sudo apt install docker.io 
```
- Установить docker-compose на сервер:
```bash
sudo apt-get update
sudo apt install docker-compose
```
- Скопировать файл docker-compose.yml и nginx.conf из директории infra на сервер:
```bash
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
```
- Для работы с Workflow добавить в Secrets GitHub переменные окружения:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

DOCKER_PASSWORD=<пароль DockerHub>
DOCKER_USERNAME=<имя пользователя DockerHub>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<ID своего телеграм-аккаунта>
TELEGRAM_TOKEN=<токен вашего бота>
```
- После деплоя изменений в git, дождитесь выполнения всех Actions.
- Зайдите на боевой сервер и выполните команды:
  * Создать суперпользователя Django
    ```bash
    sudo docker-compose exec backend python manage.py createsuperuser
    ```

- Проект будет доступен по вашему IP-адресу.

#### Авторы:
- Агукин Владимир - [https://github.com/s1gurr0s](https://github.com/s1gurr0s)
- Антипина Анастасия - [https://github.com/an-nastasiia](https://github.com/an-nastasiia)
