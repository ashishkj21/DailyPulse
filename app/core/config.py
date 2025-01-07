import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    GITHUB_APP_ID: str = os.getenv("GITHUB_APP_ID")
    GITHUB_APP_PRIVATE_KEY: str = os.getenv("GITHUB_APP_PRIVATE_KEY")
    GITHUB_REPOSITORY: str = os.getenv("GITHUB_REPOSITORY")

settings = Settings()
