import streamlit as st
import pandas as pd
import pickle

# Load saved model
model = pickle.load(open("iris_model.pkl", "rb"))
accuracy = pickle.load(open("iris_accuracy.pkl", "rb"))

st.title(" Iris Species Prediction App)")

st.write(f"### Model Accuracy: `{accuracy*100:.2f}%`")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

if st.button("Predict Species"):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)[0]

    st.success(f"### Predicted Species: **{prediction}**")