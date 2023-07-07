from fastapi import APIRouter, status


router = APIRouter(tags=["Leads"])


@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    return "SERVICE UP"
