from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func


from base_class import Base


class LeadsTable(Base):  # type: ignore
    __tablename__ = "t_leads"
    __table_args__ = {"schema": "crm"}

    lead_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    account_name = Column(String(50), nullable=False)
    office_phone = Column(String(20), nullable=False)
    email_address = Column(String(50), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now())

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name
