from app.modules.workspace.api.workspace_router import get_workspace_data


class ReportingService:
    async def get_home_workspace(self):
        return await get_workspace_data("dashboard")

    async def get_executive_workspace(self):
        return await get_workspace_data("executive")

    async def get_dashboard(self):
        return {
            "kpis": [
                {"label": "Total Customers", "value": "12,482", "change": "+6%", "positive": True, "tone": "purple", "points": [14, 18, 15, 25, 22, 33, 30, 42]},
                {"label": "KYC Pending", "value": "342", "change": "+12%", "positive": False, "tone": "pink", "points": [18, 16, 25, 20, 30, 27, 38, 44]},
                {"label": "Verified Customers", "value": "11,026", "change": "+8%", "positive": True, "tone": "blue", "points": [18, 21, 19, 28, 31, 29, 37, 44]},
                {"label": "Requires Action", "value": "612", "change": "+4%", "positive": False, "tone": "amber", "points": [12, 15, 13, 17, 20, 18, 26, 33]},
            ],
            "activity": [
                {"id": "CUST-00483", "name": "Thabo Mokoena", "status": "Verified", "date": "30 Sep 2026", "time": "14:32"},
                {"id": "CUST-00721", "name": "Lerato Dlamini", "status": "Under Review", "date": "30 Sep 2026", "time": "11:17"},
                {"id": "CUST-00316", "name": "Michael Jackson", "status": "Requires Action", "date": "29 Sep 2026", "time": "16:45"},
                {"id": "CUST-00972", "name": "Nomsa Khumalo", "status": "Verified", "date": "29 Sep 2026", "time": "09:12"},
                {"id": "CUST-01123", "name": "Jason Peterson", "status": "Pending", "date": "28 Sep 2026", "time": "16:40"},
            ],
            "verification_queue": [
                {"customer": "CUST-00483", "name": "Thabo Mokoena", "verification": "Identity verification", "priority": "High", "waiting": "2h ago", "tone": "red"},
                {"customer": "CUST-00721", "name": "Lerato Dlamini", "verification": "Proof of address", "priority": "High", "waiting": "4h ago", "tone": "red"},
                {"customer": "CUST-00316", "name": "Michael Jackson", "verification": "Document review", "priority": "Medium", "waiting": "7h ago", "tone": "amber"},
                {"customer": "CUST-01123", "name": "Jason Peterson", "verification": "Enhanced due diligence", "priority": "Medium", "waiting": "1d ago", "tone": "amber"},
            ],
            "trend": [
                {"day": "1 Sep", "verified": 280, "pending": 180, "action": 82, "started": 55},
                {"day": "5 Sep", "verified": 430, "pending": 235, "action": 105, "started": 80},
                {"day": "10 Sep", "verified": 510, "pending": 250, "action": 98, "started": 92},
                {"day": "15 Sep", "verified": 580, "pending": 310, "action": 125, "started": 108},
                {"day": "20 Sep", "verified": 610, "pending": 300, "action": 150, "started": 120},
                {"day": "25 Sep", "verified": 740, "pending": 370, "action": 178, "started": 128},
                {"day": "30 Sep", "verified": 880, "pending": 480, "action": 250, "started": 142},
            ],
            "document_types": [
                {"name": "ID Document", "value": "95%"},
                {"name": "Passport", "value": "87%"},
                {"name": "Driver's License", "value": "76%"},
                {"name": "Proof of Address", "value": "68%"},
            ],
        }

    async def get_summary(self):
        return {
            "customer_count": 5,
            "open_alert_count": 2,
            "open_case_count": 2,
            "transaction_count": 2,
        }