class CustomerRepository:
    customers = [
        {"customer_id": "CUST-00483", "first_name": "Thabo", "last_name": "Mokoena", "email": "thabo.mokoena@example.test", "country": "ZA", "customer_status": "ACTIVE", "customer_type": "INDIVIDUAL", "created_at": "2026-09-30T14:32:00Z"},
        {"customer_id": "CUST-00721", "first_name": "Lerato", "last_name": "Dlamini", "email": "lerato.dlamini@example.test", "country": "ZA", "customer_status": "UNDER_REVIEW", "customer_type": "INDIVIDUAL", "created_at": "2026-09-30T11:17:00Z"},
        {"customer_id": "CUST-00316", "first_name": "Michael", "last_name": "Jackson", "email": "michael.jackson@example.test", "country": "ZA", "customer_status": "REQUIRES_ACTION", "customer_type": "INDIVIDUAL", "created_at": "2026-09-29T16:45:00Z"},
        {"customer_id": "CUST-00972", "first_name": "Nomsa", "last_name": "Khumalo", "email": "nomsa.khumalo@example.test", "country": "ZA", "customer_status": "ACTIVE", "customer_type": "INDIVIDUAL", "created_at": "2026-09-29T09:12:00Z"},
        {"customer_id": "CUST-01123", "first_name": "Jason", "last_name": "Peterson", "email": "jason.peterson@example.test", "country": "ZA", "customer_status": "PENDING", "customer_type": "INDIVIDUAL", "created_at": "2026-09-28T16:40:00Z"},
    ]

    async def list_all(self):
        return self.customers

    async def get_by_id(self, customer_id: str):
        return next((customer for customer in self.customers if customer["customer_id"] == customer_id), None)