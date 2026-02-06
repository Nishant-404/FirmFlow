import uuid
from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class ServiceTemplate(Base):
    __tablename__ = "service_templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firm_id = Column(UUID(as_uuid=True))
    name = Column(String, nullable=False)

    # Example:
    # ["Collect Data", "Reconcile", "Prepare Return", "File Return"]
    checklist = Column(JSON)
