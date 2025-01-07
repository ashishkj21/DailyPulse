import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()
