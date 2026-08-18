import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("MODEL")
FIRE_CRAWL = os.getenv("FIRE_CRAWL_API_KEY")

OPEN_ROUTER_KEY = os.getenv("OPEN_ROUTER_KEY")
POOLSIDE_MODEL = os.getenv("POOLSIDE_MODEL")
BASE_URL = os.getenv("BASE_URL")
