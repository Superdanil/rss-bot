Описанный ниже старт программы испытан на Windows 10 и версии python 3.12.4.
На других ОС и версиях python запуск не тестировался.

Старт

1. git clone https://github.com/Superdanil/3divi_test_task
2. python3 -m venv venv
3. source venv/scripts/activate (см. ОС)
4. в файле bot/.env заполнить BOT_TOKEN
5. docker-compose up -d --build
6. начало взаимодействия с ботом командой /start
