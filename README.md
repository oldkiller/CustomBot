# CustomBot

## Общее описание
Моя реализация бота для Telegram с поддержкой плагинов (На базе данного механизма из Python 3.7).

[![Build Status](https://travis-ci.com/oldkiller/CustomBot.svg?branch=master)](https://travis-ci.com/oldkiller/CustomBot)

---------------------------------------

Для общения с серверами Telegram проект использует
[pytelegrambotapi](https://github.com/eternnoir/pyTelegramBotAPI)  

Простой пример реализации плагина

```python
from . import plugin, bot

@plugin
@bot.message_handler(commands=["test"])
def tests(msg):
    bot.send_message(msg.chat.id, "test")
```
