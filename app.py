import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer information to predict churn.")

# Inputs
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure (Months)", 0, 150, 24)
monthly_charges = st.number_input("Monthly Charges", 0.0, 500.0, 75.0)
total_charges = st.number_input("Total Charges", 0.0, 20000.0, 1800.0)

gender = st.selectbox("Gender", ["Female", "Male"])
contract = st.selectbox(
    "Contract Type",
    ["Month-to-Month", "One-Year", "Two-Year"]
)
internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber Optic", "None"]
)
support = st.selectbox("Tech Support", ["No", "Yes"])

# Prediction
if st.button("Predict Churn"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Gender_Male": [gender == "Male"],
        "ContractType_One-Year": [contract == "One-Year"],
        "ContractType_Two-Year": [contract == "Two-Year"],
        "InternetService_Fiber Optic": [internet == "Fiber Optic"],
        "InternetService_None": [internet == "None"],
        "TechSupport_Yes": [support == "Yes"]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")

