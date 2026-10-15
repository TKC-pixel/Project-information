from pydantic import BaseModel


class AlertResponse(BaseModel):
    alert_id: str
    customer_id: str
    alert_type: str
    severity: str
    status: str
    created_at: str