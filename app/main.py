from fastapi import FastAPI
from app.api.endpoints import github, slackbot

app = FastAPI()

app.include_router(github.router, prefix="/github", tags=["github"])
app.include_router(slackbot.router, prefix="/slackbot", tags=["slackbot"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
