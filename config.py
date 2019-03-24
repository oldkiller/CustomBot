import json
import os

with open("env.json", "rt") as f:
    lines = "".join(f.readlines())
    envs = json.loads(lines)

if "TELEGRAM_TOKEN" in os.environ.keys():
    tg_token = os.environ["TELEGRAM_TOKEN"]
else:
    tg_token = envs["TELEGRAM_TOKEN"]

url = ""