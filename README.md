# Kittygram

### О возможностях проекта
Kittygram — социальная сеть для обмена фотографиями любимых питомцев.

После регистрации вы можете добавить любого кота с указанием его имени, даты рождения, окраса и личных достижений. Также, каждому питомцу можно добавить фотографию.

### О проекте
Проект развернут на удалённом сервере.
Для доступа к сайту можно перейти по ссылке: https://tregalex-kittygram.ddns.net

Проект развёрнут на Ubuntu 22.04.1 с использованием системы контейнеризации при помощи утилиты Docker Compose. Архитектура контейнеризации проекта поделена на отдельные зоны ответственности: backend, frontend, gateway и db.<br>
Статика для бэкенда и фронтенда, медиафайлы, а также база данных, расположены в отдельных томах (volume): static, media и pg_data, независимо от контейнеров.<br>
При изменениях кода в главной ветке (main) репозитория, произойдёт автоматическое тестирование кода и автоматическое развертывание новой версии на удалённом сервере с помощью GitHub Actions.<br>

### Как самостоятельно развернуть проект
Для развертывания проекта необходимо в корневой директории проекта на удалённом сервере создать файл .env и добавить в него необходимые данные для переменных, по аналогии с файлом .env.example, который присутствует в репозитории.<br>
Дополнительно в корневую директорию необходимо скопировать файл docker-compose.production.yml из репозитория.<br>

Внимание! На удалённом сервере должны быть установлены утилиты Docker и Docker Compose.<br>

Запускаем Docker Compose на сервере:
```
sudo docker compose -f docker-compose.production.yml up -d
```
После запуска выполняем миграции, собираем статические файлы бэкенда и копируем их в /backend_static/static/:
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```
