import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def dashboard_view(df: pd.DataFrame):
    st.set_page_config(page_title="Dashboard", layout="wide")

    st.title("📊 Dashboard Simples")
    st.markdown("Bem-vindo ao painel de controle. Aqui estão algumas métricas e visualizações básicas.")

    # --- Métricas (cards)
    col1, col2, col3 = st.columns(3)
    col1.metric("Usuários Ativos", "1.245", "+5%")
    col2.metric("Taxa de Conversão", "3.2%", "-0.5%")
    col3.metric("Receita", "R$ 32.400", "+8%")

    st.markdown("---")

    # --- Gráfico
    st.subheader("📈 Visitas na Última Semana")

    fig, ax = plt.subplots()
    ax.plot(df["Dia"], df["Visitas"], marker='o', color='skyblue', linewidth=2)
    ax.set_title("Visitas Diárias")
    ax.set_xlabel("Data")
    ax.set_ylabel("Número de Visitas")
    ax.grid(True)
    st.pyplot(fig)

    # --- Tabela
    st.subheader("📋 Detalhes de Visitas")
    st.dataframe(df.set_index("Dia"))

