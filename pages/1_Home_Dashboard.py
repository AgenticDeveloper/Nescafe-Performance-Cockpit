import streamlit as st
from src.data import load_data
from src.ui_components import kpi_cards, donut_fleet

st.set_page_config(page_title="Home", layout="wide")
sites, machines, deployments = load_data()

st.subheader("Good morning, John! Let’s make every cup count")

total = len(deployments)
under = (deployments["cpd_actual_last7"] < deployments["cpd_expected"] * 0.9).sum()
avg_util = f"{int(100 * (deployments['cpd_actual_last7']/deployments['cpd_expected']).clip(0,1).mean())}%"
avg_roi = "22%"  # demo
kpi_cards({
    "Total Machines Deployed": total,
    "Average Utilization": avg_util,
    "Underperforming Machines": under,
    "Avg ROI per Machine": avg_roi
})

health = {
    "Green (>90% CPD)": int(((deployments["cpd_actual_last7"] / deployments["cpd_expected"]) >= 0.9).sum()),
    "Amber (70–90%)": int(((deployments["cpd_actual_last7"] / deployments["cpd_expected"]).between(0.7, 0.9)).sum()),
    "Red (<70%)": int(((deployments["cpd_actual_last7"] / deployments["cpd_expected"]) < 0.7).sum())
}

left, right = st.columns([1,2])
with left:
    st.markdown("#### Fleet Health by Tier")
    donut_fleet(health)
with right:
    st.markdown("#### Deployment Pipeline (sample)")
    st.dataframe(deployments[["site_id","model","status","months_live"]], use_container_width=True)
