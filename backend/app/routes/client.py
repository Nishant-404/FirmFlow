from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientOut

router = APIRouter(prefix="/clients", tags=["Clients"])

# TEMP firm id (until auth is added)
FAKE_FIRM_ID = "11111111-1111-1111-1111-111111111111"


@router.post("/", response_model=ClientOut)
def create_client(payload: ClientCreate, db: Session = Depends(get_db)):
    client = Client(
        firm_id=FAKE_FIRM_ID,
        name=payload.name,
        client_type=payload.client_type,
        email=payload.email,
        phone=payload.phone
    )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


@router.get("/", response_model=list[ClientOut])
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()
