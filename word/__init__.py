import os
import logging
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
import pyromod
from word.modules.word import load_words, load_common_words, load_state_city_countries


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


TOKEN = os.getenv("TOKEN", "8439042357:AAFMXd3_5-fahojjPVGBvRo4EZ7Qgr2Ldps")
mongo_url = os.getenv("MONGO_URL", "mongodb+srv://sufyan532011:5042@auctionbot.5ms20.mongodb.net/?retryWrites=true&w=majority&appName=AuctionBot")
API_HASH = os.getenv("API_HASH", "3474a18b61897c672d315fb330edb213")
API_ID = int(os.getenv("API_ID", "21218274"))   # ✅ integer banaya

if not TOKEN or not mongo_url or not API_HASH or not API_ID:
    raise ValueError("Please set the environment variables: TOKEN, MONGO_URL, API_HASH, and API_ID.")


word = Client(
    "lol",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="word"),
)


DEV_LIST = [7576729648]

client = AsyncIOMotorClient(mongo_url)
db = client["WordNWord"]
user_Collection = db["user"]
collection = db["word"]

WORD_LIST = set(load_words())
WORD_SET = set(WORD_LIST)
MEAN_WORD = load_common_words()
MEAN_WORD_SET = set(MEAN_WORD)
STATE_CITY_COUNTRY = load_state_city_countries()
COUNTRY_SET = set(STATE_CITY_COUNTRY["countries"])
STATE_SET = set(STATE_CITY_COUNTRY["states"])
CITY_SET = set(STATE_CITY_COUNTRY["cities"])
ALL_COUNTRY_SET = COUNTRY_SET | STATE_SET | CITY_SET

print(f"Loaded {len(COUNTRY_SET)} countries, {len(STATE_SET)} states, and {len(CITY_SET)} cities, and total {len(ALL_COUNTRY_SET)}.")
print(f"Loaded {len(WORD_SET)} words from the word list.")