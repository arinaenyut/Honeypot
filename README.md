# SSH Honeypot
### Инструмент, эмулирующий реальный SSH-сервер на Python, записывыющий пользователей и пароли в файл-журнал + ответ на некоторые команды
___
## Требования
- [patamiko](https://www.paramiko.org/)
- [Docker](https://www.docker.com)

## Установка

1. Сгенерировать ключи и переименовать открытый ключ
- ` ssh-keygen -t rsa -f server key `
-  ` mv server.key.pub server.pub `
2. Установка требований 
-  `run pip install -r requirements `
-  Установка [docker](https://docs.docker.com/engine/install/ubuntu/)

## Запуск

1. Создание docker image
- ` docker build -t honeypota . `
2. Запустить honeypot в doker c **-v**
- `docker run -v "${PWD}:<workdir>" -p 8080:8080 honeypot `  
 В созданном файле **logfile.log** будут отображены собранные данные
4. Подключиться к приманке
- ` ssh user@<honeypot_ip> -p 8080`

Co стороны подключения будет выдено:
###
    Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-121-generic x86_64)

       * Documentation:  https://help.ubuntu.com
       * Management:     https://landscape.canonical.com
       * Support:        https://ubuntu.com/advantage
    $ 


