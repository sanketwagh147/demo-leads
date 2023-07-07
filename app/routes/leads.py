from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db_con
from schemas.leads_schema import PostLead, PostLeadResponse
from models.leads_model import LeadsTable
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError


router = APIRouter(tags=["Leads"])


@router.post(
    "/post_leads", status_code=status.HTTP_200_OK, response_model=PostLeadResponse
)
def post_lead(lead: PostLead, db_conn: Session = Depends(get_db_con)):
    create_lead = lead.dict()

    try:
        entry = LeadsTable(**create_lead)
        s = db_conn.add(entry)
        print(s)
        db_conn.commit()
    except OperationalError as op_err:
        print(op_err)
        raise HTTPException(500, detail=op_err)

    return PostLeadResponse(status="SUCCESS")
