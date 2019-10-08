# Custom bot

## Общее описание
Моя реализация бота для Telegram с поддержкой плагинов 
(На базе данного механизма из Python 3.7).


## Зависимости
Для взаимодействия с серверами Telegram проект использует
[pytelegrambotapi](https://github.com/eternnoir/pyTelegramBotAPI).
Поэтому подробности по написанию плагинов лучше смотреть в документации 
к данной библиотеке.  
Для созданий вебморды 
использован [Flask](https://github.com/pallets/flask)  
Для иммитации переменных окружения 
использован [python-dotenv](https://github.com/theskumar/python-dotenv)


## Пример создания плагина
Плагин, который просто отправляет в чат текстовое сообщение "test" 
при получении команды "/test":
```python
from . import plugin, bot

@plugin
@bot.message_handler(commands=["test"])
def tests(msg):
    bot.send_message(msg.chat.id, "test")
```

Плагин, при получении любого текста отвечает этим же текстом на сообщение.
```python
from . import plugin, bot

@plugin
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
```

## Установка
1. Клонировать репозиторий
2. Установить зависимости из requirements.txt

## Запуск
1. Получить токен бота у [BotFather](https://telegram.me/BotFather)
2. Вставить токен бота в файл ".env". Привер приведен в файле ".env_example"
3. Запуск
    - При запуске на локальном устройстве (для тестирования) установить в 
        файле "config.py" параметр "local_run" в значение True.
    - При запуске на рабочем сервере (для использования) установить в 
        файле "config.py" параметр "local_run" в значение False.

## Планы по развитию
- Добавить базу данных
