# ==========================================
# 💼 Advanced Salary Prediction Streamlit App
# ==========================================

import streamlit as st
import pickle
import numpy as np

# ------------------------------------------
# Load Model & Encoders
# ------------------------------------------
model = pickle.load(open("salary_model.pkl", "rb"))
edu_encoder = pickle.load(open("edu_encoder.pkl", "rb"))
role_encoder = pickle.load(open("role_encoder.pkl", "rb"))

# ------------------------------------------
# Page Config
# ------------------------------------------
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="centered"
)

# ------------------------------------------
# Title
# ------------------------------------------
st.title("💼 Employee Salary Prediction App")
st.markdown("Predict salary using multiple factors")

st.divider()

# ------------------------------------------
# User Inputs
# ------------------------------------------

experience = st.slider(
    "Years of Experience",
    0, 20, 1
)

education = st.selectbox(
    "Education Level",
    ["Bachelors", "Masters", "PhD"]
)

role = st.selectbox(
    "Job Role Level",
    ["Junior", "Mid", "Senior"]
)

skills = st.slider(
    "Number of Skills",
    1, 10, 3
)

st.divider()

# ------------------------------------------
# Encode Inputs
# ------------------------------------------
edu_encoded = edu_encoder.transform([education])[0]
role_encoded = role_encoder.transform([role])[0]

input_data = np.array([[
    experience,
    edu_encoded,
    role_encoded,
    skills
]])

# ------------------------------------------
# Prediction
# ------------------------------------------
if st.button("Predict Salary 💰"):

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Salary: ₹ {prediction:,.2f}"
    )

    st.balloons()

# ------------------------------------------
# Footer
# ------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")
