import os

import plugin
from bot import bot
from webserver import server

plugin.run()


if __name__ == '__main__':
	# bot.polling(none_stop=True)
	server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
