import requests
from app.core.config import settings

def send_message(channel: str, text: str):
    headers = {"Authorization": f"Bearer {settings.SLACK_BOT_TOKEN}"}
    data = {"channel": channel, "text": text}
    response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=data)
    return response.json()
