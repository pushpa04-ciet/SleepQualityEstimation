import streamlit as st
import pickle
import numpy as np

# Load the model
with open("sleep_quality_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("💤 Sleep Quality Prediction App")

# User inputs
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=1, max_value=12, value=7)
age = st.number_input("Age", min_value=10, max_value=100, value=25)
stress_level = st.number_input("Stress Level (1-10)", min_value=1, max_value=10, value=5)
exercise_minutes = st.number_input("Exercise Minutes per Day", min_value=0, max_value=300, value=30)

# Predict button
if st.button("Predict Sleep Quality"):
    sample = np.array([[sleep_duration, age, stress_level, exercise_minutes]])
    prediction = model.predict(sample)
    st.success(f"Predicted Sleep Quality Score: {prediction[0]:.2f}")
