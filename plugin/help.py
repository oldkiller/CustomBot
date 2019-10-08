from . import plugin, bot


@plugin
@bot.message_handler(commands=["help"])
def helps(msg):
    text = "Команда /help в разработке"
    bot.send_message(msg.chat.id, text)
