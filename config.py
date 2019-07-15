import json
import os

if "TELEGRAM_TOKEN" in os.environ.keys():
    tg_token = os.environ["TELEGRAM_TOKEN"]
else:
    with open("env.json", "rt") as f:
        lines = "".join(f.readlines())
        envs = json.loads(lines)
    tg_token = envs["TELEGRAM_TOKEN"]

url = ""