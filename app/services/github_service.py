import requests
from app.core.config import settings

def fetch_commits():
    headers = {"Authorization": f"token {settings.GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/repos/your-repo/commits", headers=headers)
    return response.json()
