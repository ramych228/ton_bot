import os
from contextlib import suppress


def start_config():
    with suppress(FileNotFoundError):
        with open(f".env") as f:
            line = f.readline()
            while line:
                k, v = line.split('=', 1)
                os.environ[k] = v.strip()
                line = f.readline()


class BotConfigs:
    def __init__(self):
        self.BOT_NAMES = os.environ["BOT_NAMES"].split(",")
        self.BOT_SEEDS = {key: value for key, value in os.environ.items() if "SEED_" in key}


