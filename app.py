import streamlit as st
import pickle
import string
# https://github.com/mian828/Project-ai.git


# -----------------------------
# 1. Load Saved Model & Vectorizer
# -----------------------------
model = pickle.load(open("fake_review_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))


# -----------------------------
# 2. Text Cleaning Function
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.strip()
    return text


# -----------------------------
# 3. Streamlit UI
# -----------------------------
st.set_page_config(page_title="Fake Review Detector", layout="centered")

st.title("📝 Fake Review Detection App")
st.write("Enter a review below and the model will classify it as **Fake** or **Genuine**.")


# -----------------------------
# 4. Input Box
# -----------------------------
user_input = st.text_area("Enter Review Text", height=150)


# -----------------------------
# 5. Predict Button
# -----------------------------
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text to classify.")
    else:
        # Clean input
        cleaned = clean_text(user_input)

        # Transform text
        vector = tfidf.transform([cleaned])

        # Predict
        prediction = model.predict(vector)[0]

        # Show Result
        if prediction == 1:
            st.success("✔ The review is **Genuine**")
        else:
            st.error("✖ The review is **Fake**")
