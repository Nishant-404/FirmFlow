from pydantic import BaseModel
from uuid import UUID

class ServiceTemplateCreate(BaseModel):
    name: str
    checklist: list[str]

class ServiceTemplateOut(BaseModel):
    id: UUID
    firm_id: UUID
    name: str
    checklist: list[str]

    class Config:
        from_attributes = True
