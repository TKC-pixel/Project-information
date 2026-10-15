class ScreeningRepository:
    results = [
        {"id": "SCR-008421", "customer": "Thabo Mokoena", "customerId": "CUST-00483", "source": "Sanctions", "status": "Clear", "score": "2%", "time": "12 min ago"},
        {"id": "SCR-008420", "customer": "Lerato Dlamini", "customerId": "CUST-00721", "source": "PEP", "status": "Potential Match", "score": "78%", "time": "24 min ago"},
        {"id": "SCR-008419", "customer": "Michael Jackson", "customerId": "CUST-00316", "source": "Adverse Media", "status": "Escalated", "score": "91%", "time": "42 min ago"},
        {"id": "SCR-008418", "customer": "Nomsa Khumalo", "customerId": "CUST-00972", "source": "Sanctions", "status": "Clear", "score": "4%", "time": "1h ago"},
        {"id": "SCR-008417", "customer": "Jason Peterson", "customerId": "CUST-01123", "source": "PEP", "status": "Under Review", "score": "64%", "time": "2h ago"},
    ]

    async def list_all(self):
        return self.results

    async def get_customer_screening(self, customer_id: str):
        return [result for result in self.results if result["customerId"] == customer_id]

    async def get_dashboard(self):
        return {
            "kpis": [
                {"label": "Total Screened", "value": "18,642", "change": "+9.4%", "positive": True, "tone": "purple"},
                {"label": "Potential Matches", "value": "128", "change": "+16.8%", "positive": False, "tone": "pink"},
                {"label": "Cleared", "value": "18,201", "change": "+8.9%", "positive": True, "tone": "blue"},
                {"label": "Escalated", "value": "74", "change": "+11.2%", "positive": False, "tone": "amber"},
            ],
            "trend": [
                {"day": "1 Sep", "screened": 2100, "matches": 32},
                {"day": "5 Sep", "screened": 2700, "matches": 41},
                {"day": "10 Sep", "screened": 3100, "matches": 38},
                {"day": "15 Sep", "screened": 3550, "matches": 52},
                {"day": "20 Sep", "screened": 4020, "matches": 47},
                {"day": "25 Sep", "screened": 4620, "matches": 61},
                {"day": "30 Sep", "screened": 5240, "matches": 68},
            ],
            "breakdown": [
                {"name": "No Match", "value": 18201},
                {"name": "Potential Match", "value": 128},
                {"name": "Confirmed Match", "value": 74},
                {"name": "Under Review", "value": 239},
            ],
            "sources": [
                {"name": "Sanctions", "matches": 42, "percentage": 82},
                {"name": "PEP", "matches": 31, "percentage": 67},
                {"name": "Adverse Media", "matches": 28, "percentage": 58},
                {"name": "Law Enforcement", "matches": 15, "percentage": 41},
                {"name": "Other Watchlists", "matches": 12, "percentage": 32},
            ],
            "results": self.results,
            "queue": [
                {"title": "Potential sanctions match", "detail": "3 customers require manual review", "priority": "High", "tone": "red"},
                {"title": "PEP matches detected", "detail": "5 profiles require enhanced screening", "priority": "Medium", "tone": "amber"},
                {"title": "Adverse media review", "detail": "7 customer profiles require investigation", "priority": "Medium", "tone": "purple"},
            ],
        }