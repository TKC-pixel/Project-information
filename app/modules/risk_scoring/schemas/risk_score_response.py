from pydantic import BaseModel

from app.modules.risk_scoring.schemas.risk_event_response import RiskEventResponse


class RiskScoreResponse(BaseModel):
    customer_id: str
    score: float
    risk_level: str
    scoring_method: str
    model_version: str
    calculated_at: str
    risk_events: list[RiskEventResponse]