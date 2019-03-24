from . import plugin, bot

@plugin
@bot.message_handler(commands=["id"])
def ids(msg):
    text = "ID " + msg.from_user.first_name \
        +" "+ msg.from_user.last_name + ": " \
        + str(msg.from_user.id)
    bot.send_message(msg.chat.id, text)