import streamlit as st

from pages.dashboard import show_dashboard
from pages.prediction import show_prediction_page
from pages.comparison import show_comparison

st.set_page_config(
    page_title="Arabic News Analyzer",
    layout="wide"
)

st.sidebar.title(
    "Arabic News Analyzer"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Prediction",
        "Comparison"
    ]
)

if page == "Dashboard":
    show_dashboard()

elif page == "Prediction":
    show_prediction_page()

elif page == "Comparison":
    show_comparison()