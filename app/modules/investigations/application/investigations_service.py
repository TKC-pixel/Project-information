from app.modules.workspace.api.workspace_router import get_workspace_data


class InvestigationsService:
    async def get_workspace_dashboard(self):
        return await get_workspace_data("investigations")

    async def list_cases(self):
        return [
            {"case_id": "CASE-001", "customer_id": "CUST-00316", "alert_id": "ALT-001", "status": "OPEN", "priority": "HIGH", "outcome": None, "opened_at": "2026-09-29T17:00:00Z"},
            {"case_id": "CASE-002", "customer_id": "CUST-00721", "alert_id": "ALT-002", "status": "IN_REVIEW", "priority": "MEDIUM", "outcome": None, "opened_at": "2026-09-30T12:00:00Z"},
        ]