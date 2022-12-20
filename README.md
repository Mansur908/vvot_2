# Нургалеев Мансур 11-907

Пояснение для запуска системы:
- 1 Создать бакет с именем itis-2022-2023-vvot33-photos в сервисе «Yandex Object Storage»
- 2 Создать облачную функцию с именем vvot33-face-detection в сервисе «Yandex Cloud Functions» и скопировать содержимое файла из репозитория с аналогичным названием.
Добавить файл requirements.txt с необходимыми библиотеками, добавить в переменные окружения значения AWS_ACCESS_KEY_ID и AWS_SECRET_ACCESS_KEY взятые из сервисного аккаунта с ролью admin.
- 3 Создать триггер с именем vvot33-photo-trigger с настройками как на картине с названием vvot33-photo-trigger в репозитории.
- 4 Создать очередь с именем vvot33-tasks в сервисе «Yandex Message Queue». Добавить в переменные окружения облачной функции vvot33-face-detection значение QueueUrl из недавно созданной очереди vvot33-tasks.



- Создать базу даннынных vvot33-db-photo-face в сервисе «Yandex Managed Service for YDB» и в ней создать таблицу с именем faces со структурой как на фото vvot00-db-photo-face в репозитории.
- Создать Api шлюз с именем itis-2022-2023-vvot33-api в сервисе «API Gateway» и скопировать содержимое yml файла из репозитория.
- Создать облачную функцию с именем vvot33-boot в сервисе «Yandex Cloud Functions» и скопировать содержимое файла из репозитория с аналогичным названием.
Добавить файл requirements.txt с необходимыми библиотеками, добавить в переменные окружения значения AWS_ACCESS_KEY_ID и AWS_SECRET_ACCESS_KEY взятые из сервисного аккаунта с ролью admin, YDB_DATABASE и YDB_ENDPOINT взятые из параметров базы данных vvot33-db-photo-face, API_GATEWAY служебный домен взятый из itis-2022-2023-vvot33-api
- В Telegram создать бота с помощью BotFather м получить token. Далее создать Webhook вставив значения в ссылку и перейти по ссылке в браузере.
ссылка: https://api.telegram.org/bot{токен бота}/setWebhook?url={Ссылка для вызова функции vvot33-boot}
