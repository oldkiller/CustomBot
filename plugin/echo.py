from . import plugin, bot

@plugin
@bot.message_handler(commands=["echo"])
def echo(msg):
    bot.send_message(msg.chat.id, msg.text)