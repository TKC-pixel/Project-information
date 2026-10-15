from pydantic import BaseModel


class RiskEventResponse(BaseModel):
    risk_category: str
    risk_type: str
    contribution: float
    description: str