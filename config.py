#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "26986162")
        self.API_HASH: str = os.environ.get("API_HASH", "c63fcc05044560910d6f0f6cccec9411")
        self.SESSION: str = os.environ.get("SESSION", "AQCjB39oNSoSViVzktiC5TH3Pcmsix55-5dlpVJdbJ72OwpZOZN_iFh2ENDewYfkcMkQ1GjqCNeFUdFp05QuMQ5Z5JTX1Lmh4jNG8oM3iK1o3lvTZcAukkI_3dZyczrwTm6nd3jWilVEwU3ybKGIkrcG9k7wCZVJxujL6bnicEH32nNrffRvfGM63ei-k0jnTPl52y4fGyPWyT5eBbGUHHR2kLj-opkeDnDnwud0jD2WbO4_TpnuxAizRRKJ5PU8fjKv7GJfadmIGFE7I2vco1GKlZTju-57ekLxfS3S7497fZv-v5TZAJA3B46LS11YHQwPkg3nC2o300GCbo0QaT3xAAAAAUrKF3AA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5549725552").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
