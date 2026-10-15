from app.modules.workspace.api.workspace_router import get_workspace_data


class TransactionMonitoringService:
    async def get_workspace_dashboard(self):
        return await get_workspace_data("transactions")

    async def list_transactions(self):
        return [
            {"financial_transaction_id": "TXN-001", "customer_id": "CUST-00483", "account_id": "ACC-001", "transaction_type": "DEPOSIT", "transaction_amount": 2500.0, "transaction_timestamp": "2026-09-30T14:00:00Z"},
            {"financial_transaction_id": "TXN-002", "customer_id": "CUST-00316", "account_id": "ACC-002", "transaction_type": "WITHDRAWAL", "transaction_amount": 8700.0, "transaction_timestamp": "2026-09-30T13:20:00Z"},
        ]