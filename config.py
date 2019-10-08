import os

# telegram token search
if "TELEGRAM_TOKEN" in os.environ.keys():
    tg_token = os.environ["TELEGRAM_TOKEN"]
else:
    import dotenv
    dotenv.load_dotenv()
    tg_token = os.environ["TELEGRAM_TOKEN"]

# heroku url
url = ""

# For running on local machine
local_run = False
