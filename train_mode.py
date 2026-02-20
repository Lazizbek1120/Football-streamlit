import streamlit as st
import numpy as np
import joblib
import sklearn

# Yuklash
model = joblib.load(r"C:\Users\HP\Desktop\Lazizbek\Osimliklar\plant_model.pkl")
scaler = joblib.load(r"C:\Users\HP\Desktop\Lazizbek\Osimliklar\scaler.pkl")
le = joblib.load(r"C:\Users\HP\Desktop\Lazizbek\Osimliklar\label_encoder.pkl")
feature_names = joblib.load(r"C:\Users\HP\Desktop\Lazizbek\Osimliklar\feature_names.pkl")

st.title(" plant")

st.write("O‘simlik parametrlarini kiriting:")

inputs = []

for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0)
    inputs.append(value)

if st.button("Predict"):
    input_array = np.array([inputs])
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)
    result = le.inverse_transform(prediction)

    proba = model.predict_proba(input_scaled)
    confidence = np.max(proba) * 100

    st.success(f" Kasallik: {result[0]}")
    st.info(f"Ishonchlilik: {confidence:.2f}%")


