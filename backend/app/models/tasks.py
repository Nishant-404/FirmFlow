import uuid
from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    service_instance_id = Column(UUID(as_uuid=True), ForeignKey("service_instances.id"))
    name = Column(String)
    assigned_to = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    due_date = Column(Date)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
