from fastapi import APIRouter

router = APIRouter()

@router.get("/commits")
def get_commits():
    # Logic to fetch commits from GitHub
    return {"commits": "List of commits"}
