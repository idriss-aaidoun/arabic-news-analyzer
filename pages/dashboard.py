import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():

    st.header("Dataset Dashboard")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.dataframe(df.head())

        st.metric(
            "Rows",
            df.shape[0]
        )

        st.metric(
            "Columns",
            df.shape[1]
        )

        sentiment_col = st.selectbox(
            "Sentiment Column",
            df.columns
        )

        fig = px.histogram(
            df,
            x=sentiment_col
        )

        st.plotly_chart(fig)