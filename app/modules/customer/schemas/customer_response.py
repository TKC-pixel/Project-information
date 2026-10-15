from pydantic import BaseModel


class CustomerResponse(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    country: str
    customer_status: str
    customer_type: str
    created_at: str