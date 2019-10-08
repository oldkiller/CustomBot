import os

import plugin
import config
from bot import bot
from webserver import server

plugin.run()


if __name__ == '__main__':
	if config.local_run:
		bot.polling(none_stop=True)
	else:
		server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
