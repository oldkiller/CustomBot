import hashlib

from flask import Flask, request, render_template
import telebot

from bot import bot
import config

server = Flask(__name__)


@server.route("/bot", methods=["POST"])
def get_message():
	upd = [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
	bot.process_new_updates(upd)
	return "Create and process new updates", 200


@server.route("/")
def webhook_add():
	return render_template("index.html")
	# bot.remove_webhook()
	# bot.set_webhook(url=config.url)
	# return "!", 200


@server.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
	if request.method == "POST":
		bot.remove_webhook()
		bot.set_webhook(url=config.url)
		return "Webhook set successful", 200
	else:
		return f"Get to the main page. <a href=\"/\">Main page</a>", 400


@server.route("/remove_webhook", methods=["GET", "POST"])
def remove_webhook():
	if request.method == "POST":
		passwd = bytes(request.form["password"], encoding="utf-8")
		hashwd = hashlib.md5(passwd).hexdigest()
		if hashwd == "5b4ae01462b2930e129e31636e2fdb68":
			bot.remove_webhook()
			return "Webhook removed successful", 200
		else:
			return "Bad password", 401
	else:
		return "Get to the main page and enter password " \
			"in the appropriate form. <a href=\"/\">Main page</a>", 400
	# paswd = hashlib.md5(bytes(password, encoding="utf-8")).hexdigest()
	# if paswd == "5b4ae01462b2930e129e31636e2fdb68":
	# 	bot.remove_webhook()
	# 	return "Webhook removed", 200
	# else:
	# 	return "Invalid password", 200


if __name__ == '__main__':
	server.run()
