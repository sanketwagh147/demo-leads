
from fastapi import APIRouter, HTTPException, status


router = APIRouter(tags=["Leads"])
@router.post("/post_leads", status_code = status.HTTP_200_OK)
def post_leads():
    
    
