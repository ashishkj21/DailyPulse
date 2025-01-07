from pydantic import BaseModel

class SlackMessage(BaseModel):
    user: str
    text: str
    channel: str
