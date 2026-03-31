from fastapi import APIRouter
from backend.services.summary_service import get_summary
router = APIRouter()

@router.get("/summary/{user_id}")
def read_summary(user_id: str, timeframe: str = "weekly"):
    return get_summary(user_id, timeframe)

