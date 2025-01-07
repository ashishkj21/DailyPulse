from fastapi import APIRouter
from app.services.github_service import get_commits, get_pull_requests

router = APIRouter()

@router.get("/commits")
def fetch_commits():
    commits = get_commits()
    return {"commits": commits}

@router.get("/pull_requests")
def fetch_pull_requests():
    prs = get_pull_requests()
    return {"pull_requests": prs}
