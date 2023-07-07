from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db_con
from schemas.leads_schema import PostLead
from sqlalchemy.orm import Session
import database


router = APIRouter(tags=["Leads"])


@router.post("/post_leads", status_code=status.HTTP_200_OK)
def post_lead(lead: PostLead, db_conn: Session = Depends(database.get_db_con)):
    pass
