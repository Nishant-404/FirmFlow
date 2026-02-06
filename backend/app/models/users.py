import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy import String

from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    firm_id = Column(UUID(as_uuid=True), ForeignKey("firms.id"))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="staff")  # admin, staff
    created_at = Column(DateTime, default=datetime.utcnow)
