import os
from fastapi import Request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv
from app.functions import collect_standup_update

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
handler = SlackRequestHandler(app)

@app.event("app_mention")
def handle_mentions(event, say):
    user_id = event['user']
    slack_token = os.getenv('SLACK_BOT_TOKEN')
    text = event['text']
    
    say("Sure, I'll get right on that!")
    response = collect_standup_update(text, user_id, slack_token)
    say(response)

async def handle_slack_event(request: Request):
    return await handler.handle(request)
