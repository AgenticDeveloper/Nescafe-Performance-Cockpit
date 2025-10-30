import streamlit as st

st.set_page_config(page_title="Analytics & Learning", layout="wide")
st.subheader("Analytics & Learning Center")
st.metric("Prediction Accuracy (demo)", "86%")
st.metric("Intervention Success Rate (demo)", "61%")

st.markdown("Rate the usefulness of recent recommendations:")
st.slider("Usefulness", 1, 5, 4)
st.success("Thanks! Feedback logged for continuous learning (demo).")
