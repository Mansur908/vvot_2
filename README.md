# Нургалеев Мансур 11-907

Пояснение для запуска системы:
- Создать бакет с именем ```itis-2022-2023-vvot33-photos``` в сервисе «Yandex Object Storage»
- Создать облачную функцию с именем ```vvot33-face-detection``` в сервисе «Yandex Cloud Functions» и скопировать содержимое файла из репозитория с аналогичным названием.
Добавить файл requirements.txt с необходимыми библиотеками, добавить в переменные окружения значения AWS_ACCESS_KEY_ID и AWS_SECRET_ACCESS_KEY взятые из сервисного аккаунта с ролью admin.
- Создать триггер с именем ```vvot33-photo-trigger``` с настройками как на картине с названием ```vvot33-photo-trigger``` в репозитории.
- Создать очередь с именем ```vvot33-tasks``` в сервисе «Yandex Message Queue». Добавить в переменные окружения облачной функции ```vvot33-face-detection``` значение QueueUrl из недавно созданной очереди ```vvot33-tasks```.
- Создать бакет с именем ```itis-2022-2023-vvot33-faces```
- Создать базу даннынных ```vvot33-db-photo-face``` в сервисе «Yandex Managed Service for YDB» и в ней создать таблицу с именем faces со структурой как на фото ```vvot33-db-photo-face``` в репозитории.
- Создать Api шлюз с именем ```itis-2022-2023-vvot33-api``` в сервисе «API Gateway» и скопировать содержимое yml файла из репозитория.

- Создать реестр Container Registry командой в консоли:

```yc container registry create --name my-first-registry``` 

- Сконфигурировать докер командой:

```yc container registry configure-docker```

- Скачать файлы dockerfile и index.py из репозитория и поместить в одну папку.
Сгенерировать файл сервисного аккаунта командой: 

```yc iam key create --folder-id {folder-id} --service-account-name vvot33-admin --output /vvot33-admin.json```

- Создать образ коммандой 

```docker build . -t cr.yandex/crpeus0hurv22o1jdcbu/vvot33```

И загрузить

```docker push cr.yandex/crpeus0hurv22o1jdcbu/vvot33:latest```

- Создать контейнер ```vvot33-face-cut``` по загруженному образу и с переменными окружения 
```AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, SA_KEY_FILE=/vvot33-admin.json```

- Создать тригер с именем ```vvot33-task-trigger``` с настройками как на картине с названием ```vvot33-task-trigger``` в репозитории.
- Создать облачную функцию с именем ```vvot33-boot``` в сервисе «Yandex Cloud Functions» и скопировать содержимое файла из репозитория с аналогичным названием.
Добавить файл requirements.txt с необходимыми библиотеками, добавить в переменные окружения значения AWS_ACCESS_KEY_ID и AWS_SECRET_ACCESS_KEY взятые из сервисного аккаунта с ролью admin, YDB_DATABASE и YDB_ENDPOINT взятые из параметров базы данных ```vvot33-db-photo-face```, API_GATEWAY служебный домен взятый из ```itis-2022-2023-vvot33-api```
- В Telegram создать бота с помощью @BotFather получить token. Далее создать Webhook вставив значения в ссылку и перейти по ссылке в браузере.
ссылка: ```https://api.telegram.org/bot{токенБота}/setWebhook?url={СсылкаДляВызоваФункции"vvot33-boot"}```
