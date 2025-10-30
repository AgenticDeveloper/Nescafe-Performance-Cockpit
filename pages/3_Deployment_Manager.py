import streamlit as st
from src.data import load_data

st.set_page_config(page_title="Deployment Manager", layout="wide")
sites, machines, deployments = load_data()

st.subheader("Deployment Manager")
st.markdown("Guardrails: ROI > 15%, Rebate < 5%, Stock available, Credit ≥ B-")

st.dataframe(
    deployments.merge(sites[["id","name"]], left_on="site_id", right_on="id")
    .rename(columns={"name":"Site Name"})[
        ["Site Name","model","cpd_expected","cpd_actual_last7","status","months_live","contract"]
    ],
    use_container_width=True
)

st.markdown("#### Scenario Simulator (demo)")
roi_target = st.slider("ROI threshold (%)", 5, 40, 15)
st.success(f"Configurations meeting ROI ≥ {roi_target}%: **2** (demo)")
st.button("Approve selected deployment(s)")
