import os
from contextlib import suppress

with suppress(FileNotFoundError):
    with open(f".env") as f:
        line = f.readline()
        while line:
            k, v = line.split('=', 1)
            os.environ[k] = v.strip()
            line = f.readline()


class BotConfigs:
    BOT_NAMES = os.environ["BOT_NAMES"].split(",")
    BOT_SEEDS = {key: value for key, value in os.environ.items() if "SEED_" in key}


class GameConfig:
    pass
