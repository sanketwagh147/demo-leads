from pydantic import BaseModel, EmailStr


class PostLead(BaseModel):
    first_name: str
    last_name: str
    account_name: str
    office_phone: str
    email_address: EmailStr


class PostLeadResponse(BaseModel):
    status: str
