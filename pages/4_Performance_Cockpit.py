import streamlit as st
from src.data import load_data
from src.logic import next_best_actions

st.set_page_config(page_title="Performance Cockpit", layout="wide")
sites, machines, deployments = load_data()

st.subheader("Performance Cockpit")
st.dataframe(
    deployments.merge(sites[["id","name"]], left_on="site_id", right_on="id")
    .rename(columns={"name":"Customer / Site"})[
        ["Customer / Site","model","cpd_expected","cpd_actual_last7","uptime_pct","status"]
    ],
    use_container_width=True
)

st.markdown("#### Root Cause & Interventions")
row = deployments.iloc[0]
actions = next_best_actions(row["cpd_expected"], row["cpd_actual_last7"], row["uptime_pct"])
for a in actions:
    st.warning(f"{a['action']} — {a['reason']} | Expected uplift: {a['expected_uplift']} CPD")
st.button("Execute interventions (log demo)")
