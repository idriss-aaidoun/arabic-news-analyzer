import re

def clean_arabic_text(text):

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\d+", "", text)

    text = text.replace("أ", "ا")
    text = text.replace("إ", "ا")
    text = text.replace("آ", "ا")

    text = re.sub(r"\s+", " ", text)

    return text.strip()