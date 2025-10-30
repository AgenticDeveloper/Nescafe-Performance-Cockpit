import streamlit as st
import plotly.express as px
import pandas as pd

def kpi_cards(metrics: dict, cols=4):
    c = st.columns(cols)
    for i, (k, v) in enumerate(metrics.items()):
        with c[i % cols]:
            st.metric(k, v)

def donut_fleet(health_counts: dict):
    df = pd.DataFrame({"tier": list(health_counts), "count": list(health_counts.values())})
    fig = px.pie(df, values="count", names="tier", hole=0.55)
    st.plotly_chart(fig, use_container_width=True)
