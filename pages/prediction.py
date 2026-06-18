import streamlit as st

from models.sentiment_model import predict_sentiment
from models.keyword_extractor import extract_keywords

def show_prediction_page():

    st.header("Arabic Sentiment Analysis")

    text = st.text_area(
        "Paste Arabic Text",
        height=200
    )

    if st.button("Analyze"):

        result = predict_sentiment(text)

        st.subheader("Sentiment")

        st.write(result["label"])

        st.progress(float(result["score"]))

        st.write(
            f"Confidence : {result['score']:.2%}"
        )

        st.subheader("Keywords")

        keywords = extract_keywords(text)

        for word, score in keywords:
            st.write(word)