from pydantic import BaseModel


class KycResponse(BaseModel):
    customer_id: str
    identity_status: str
    address_status: str
    verification_result: str