# Django + Stripe system

## Описание

Django проект, реализующий Stripe в Django системе

Протестирорвать проект можно по ссылке
```sh
http://minky.pythonanywhere.com/item/<id>
```
Выбираем id от 1 до 3
## Установка необходимых зависимостей

Для корректной работы необходимо иметь установленный docker и docker-compose

Пример установки на Ubuntu:
```sh
https://docs.docker.com/engine/install/ubuntu/
```
Так-же нужно получить две пары Stripe API ключей разных волют
```sh
https://dashboard.stripe.com/test/apikeys
```

## Настройка и запуск
### Пердварительная настройка
Клонируем репозиторий и изменяем некоторые настройки
- Открываем файл ***.env*** в папке ***testWorkDjango*** и вставляем наши API ключи
### Запуск
Запускаем контейнер
```sh
sudo docker-compose up --build -d
```
И переходим по адрессу 
```sh
http://0.0.0.0:8000/item/<id>
```

Для добовления новых обьектов переходим 
```sh
http://0.0.0.0:8000/admin
```
Создан админ с логином: ***admin*** и поролем: ***123***, но можно создать своего

