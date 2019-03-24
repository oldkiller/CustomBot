# CustomBot

Моя реализация бота с поддержкой плагинов.

---------------------------------------

Для общения с серверами Telegram проект использует
[pytelegrambotapi](https://github.com/eternnoir/pyTelegramBotAPI)  

Простой пример реализации плагина

```python
from . import plugin, bot

@plugin
@bot.message_handler(commands=["test"])
def ids(msg):
    bot.send_message(msg.chat.id, "test")
```