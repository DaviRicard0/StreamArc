import pandas as pd
from src.web.views.dashboard_view import dashboard_view

class DashboardController:
    def execute(self):
        df = pd.DataFrame({
            "Dia": pd.date_range(start="2025-05-01", periods=7),
            "Visitas": [150, 200, 180, 220, 240, 210, 300]
        })

        dashboard_view(df)

if __name__ == "__main__":
    DashboardController().execute()