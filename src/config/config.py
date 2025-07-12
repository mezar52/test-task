import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
DATABASE_URL     = os.getenv("DATABASE_URL")
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY")