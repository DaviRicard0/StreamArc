import pandas as pd
import streamlit as st
from docling.document_converter import DocumentConverter

from src.web.views.dashboard_view import dashboard_view

class DashboardController:
    def execute(self):
        source = "https://arxiv.org/pdf/2408.09869"  # PDF path or URL
        converter = DocumentConverter()
        result = converter.convert(source)
        st.write(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"

        df = pd.DataFrame({
            "Dia": pd.date_range(start="2025-05-01", periods=7),
            "Visitas": [150, 200, 180, 220, 240, 210, 300]
        })

        dashboard_view(df)

if __name__ == "__main__":
    DashboardController().execute()