class KycRepository:
    records = [
        {"customer_id": "CUST-00483", "identity_status": "VERIFIED", "address_status": "VERIFIED", "verification_result": "PASS"},
        {"customer_id": "CUST-00721", "identity_status": "PENDING", "address_status": "PENDING", "verification_result": "IN_REVIEW"},
        {"customer_id": "CUST-00316", "identity_status": "REJECTED", "address_status": "REJECTED", "verification_result": "ACTION_REQUIRED"},
        {"customer_id": "CUST-00972", "identity_status": "VERIFIED", "address_status": "VERIFIED", "verification_result": "PASS"},
        {"customer_id": "CUST-01123", "identity_status": "PENDING", "address_status": "PENDING", "verification_result": "IN_REVIEW"},
    ]

    async def list_all(self):
        return self.records

    async def get_customer_kyc(self, customer_id: str):
        return next((record for record in self.records if record["customer_id"] == customer_id), None)