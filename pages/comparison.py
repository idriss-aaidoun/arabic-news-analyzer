import streamlit as st
import pandas as pd
import plotly.express as px

def show_comparison():

    st.header("Model Comparison")

    results = pd.DataFrame(
        {
            "Model":[
                "Logistic Regression",
                "SVM",
                "AraBERT",
                "MARBERT"
            ],
            "Accuracy":[
                0.78,
                0.82,
                0.91,
                0.93
            ]
        }
    )

    fig = px.bar(
        results,
        x="Model",
        y="Accuracy"
    )

    st.plotly_chart(fig)

    st.dataframe(results)