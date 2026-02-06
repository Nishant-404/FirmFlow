from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.service_template import ServiceTemplate
from app.schemas.service_template import ServiceTemplateCreate, ServiceTemplateOut

router = APIRouter(prefix="/service-templates", tags=["ServiceTemplates"])

# TEMP firm id (until auth is added)
FAKE_FIRM_ID = "11111111-1111-1111-1111-111111111111"


@router.post("/", response_model=ServiceTemplateOut)
def create_service_template(payload: ServiceTemplateCreate, db: Session = Depends(get_db)):
    template = ServiceTemplate(
        firm_id=FAKE_FIRM_ID,
        name=payload.name,
        checklist=payload.checklist
    )
    db.add(template)
    db.commit()
    db.refresh(template)
    return template


@router.get("/", response_model=list[ServiceTemplateOut])
def list_service_templates(db: Session = Depends(get_db)):
    return db.query(ServiceTemplate).all()
