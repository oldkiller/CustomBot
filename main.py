import hashlib
import config
# import flask
import os

import plugin
from bot import bot

plugin.run()

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "hello")

# server = flask.Flask(__name__)

# @server.route("/bot", methods=["POST"])
# def get_message():
# 	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
# 	return "!", 200

# @server.route("/")
# def webhook_add():
# 	bot.remove_webhook()
# 	bot.set_webhook(url=config.url)
# 	return "!", 200

# @server.route("/<password>")
# def webhook_rem(password):
# 	pasw = hashlib.md5(bytes(password, encoding="utf-8")).hexdigest()
# 	if pasw == "5b4ae01462b2930e129e31636e2fdb68":
# 		bot.remove_webhook()
# 		return "Webhook removed", 200
# 	else:
# 		return "Invalid password", 200

# server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.polling(none_stop=True)