from pydantic import BaseModel
from uuid import UUID

class ClientCreate(BaseModel):
    name: str
    client_type: str
    email: str | None = None
    phone: str | None = None

class ClientOut(BaseModel):
    id: UUID
    name: str
    client_type: str
    email: str | None
    phone: str | None

    class Config:
        from_attributes = True
