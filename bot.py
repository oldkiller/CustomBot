import telebot
import config

bot = telebot.TeleBot(config.tg_token)


@bot.message_handler(commands=["start"])
def start(msg):
	bot.send_message(msg.chat.id, "hello")
