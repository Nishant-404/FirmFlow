import uuid
from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.database import Base

class ServiceInstance(Base):
    __tablename__ = "service_instances"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    template_id = Column(UUID(as_uuid=True), ForeignKey("service_templates.id"))
    period = Column(String)  # e.g. April-2026
    due_date = Column(Date)
    status = Column(String, default="pending")  # pending/in_progress/completed
    created_at = Column(DateTime, default=datetime.utcnow)
