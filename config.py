from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29565918))
API_HASH = getenv("API_HASH", "031c82d93ff3cb7d9711ba2ec4d4a9ec")

BOT_TOKEN = getenv("BOT_TOKEN", "6567617162:AAHjMwCr1jRIO_IGIb3JfNB-ihGJ_giyQWU")
