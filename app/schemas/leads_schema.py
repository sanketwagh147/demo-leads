from pydantic import BaseModel, EmailStr


class PostLead(BaseModel):
    first_name: str
    last_name: str
    account_name: str
    phone_office: str
    email_address: EmailStr
