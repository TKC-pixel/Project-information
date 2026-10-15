from pydantic import BaseModel


class ScreeningResponse(BaseModel):
    id: str
    customer: str
    customerId: str
    source: str
    status: str
    score: str
    time: str