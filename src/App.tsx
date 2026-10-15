import {
    BrowserRouter,
    Navigate,
    Route,
    Routes,
} from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import DashboardHome from "./pages/DashboardHome";
import RiskScreening from "./pages/RiskScreening";
import TransactionMonitoring from "./pages/TransactionMonitoring";
import KycMonitoring from "./pages/KycMonitoring";
import NetworkIntelligence from "./pages/NetworkIntelligence";
import AlertQueue from "./pages/AlertQueue";
import InvestigationWorkspace from "./pages/InvestigationWorkspace";
import ExecutiveDashboard from "./pages/ExecutiveDashboard";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />

                <Route path="/register" element={<Register />} />

                <Route path="/" element={<Navigate to="/dashboard" replace />} />
                <Route path="/dashboard" element={<DashboardHome />} />
                <Route path="/screening" element={<RiskScreening />} />
                <Route path="/transactions" element={<TransactionMonitoring />} />
                <Route path="/kyc" element={<KycMonitoring />} />
                <Route path="/network" element={<NetworkIntelligence />} />
                <Route path="/alerts" element={<AlertQueue />} />
                <Route path="/investigations" element={<InvestigationWorkspace />} />
                <Route path="/executive" element={<ExecutiveDashboard />} />

                <Route
                    path="*"
                    element={<Navigate to="/login" replace />}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;