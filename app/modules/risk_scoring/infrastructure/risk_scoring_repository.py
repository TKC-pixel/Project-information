class RiskScoringRepository:
    scores = {
        "CUST-00316": {
            "customer_id": "CUST-00316",
            "score": 82,
            "risk_level": "HIGH",
            "scoring_method": "MOCK",
            "model_version": "mock-1",
            "calculated_at": "2026-09-30T15:00:00Z",
            "risk_events": [
                {"risk_category": "SCREENING", "risk_type": "ADVERSE_MEDIA_MATCH", "contribution": 82, "description": "Sample screening risk event"}
            ],
        },
        "CUST-00483": {
            "customer_id": "CUST-00483",
            "score": 24,
            "risk_level": "LOW",
            "scoring_method": "MOCK",
            "model_version": "mock-1",
            "calculated_at": "2026-09-30T15:00:00Z",
            "risk_events": [],
        },
    }

    async def get_by_customer_id(self, customer_id: str):
        return self.scores.get(customer_id)