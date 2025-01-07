from fastapi import APIRouter, Request
from app.services.slack_service import handle_slack_event

router = APIRouter()

@router.post("/events")
async def slack_events(request: Request):
    return await handle_slack_event(request)
