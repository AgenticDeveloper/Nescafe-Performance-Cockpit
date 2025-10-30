import streamlit as st
import pandas as pd
from src.data import load_data
from src.logic import predict_cpd, fit_score, roi_percent

st.set_page_config(page_title="Opportunity Analyzer", layout="wide")
sites, machines, _ = load_data()

st.subheader("Opportunity Analyzer")
site = st.selectbox("Select a prospect site", sites["name"])
row = sites[sites["name"] == site].iloc[0]
pred_cpd, conf = predict_cpd(row)
st.info(f"Predicted CPD for **{site}**: **{pred_cpd}**  |  Confidence: **{conf}%**")

st.markdown("#### AI Recommendations (Best-fit machine & ROI)")
recs = []
for _, m in machines.iterrows():
    score, util = fit_score(pred_cpd, m)
    roi = roi_percent(pred_cpd, m)
    recs.append({"model": m["model"], "fit_score": score, "utilization": f"{int(util*100)}%", "roi_%": roi})

df = pd.DataFrame(recs).sort_values("fit_score", ascending=False)
st.dataframe(df, use_container_width=True)
st.button("Save Opportunity")
