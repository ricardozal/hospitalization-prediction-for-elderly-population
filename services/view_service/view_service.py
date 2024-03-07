import streamlit as st
import numpy as np
import pandas as pd
from uuid import uuid4
from gateway import predict_hospitalization, predict_hospitalization_bunch


def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error processing file: {e}")
            return None
    return None


st.title('Hospitalization Prediction Form')

uploaded_file = st.file_uploader("Upload an Excel file with the health data", type=["xlsx"])

if uploaded_file is not None:
    data_df = process_uploaded_file(uploaded_file)
    if data_df is not None:
        predictions = predict_hospitalization_bunch(data_df)
        data_df['Will be hospitalized'] = predictions
        st.write("Prediction Results:")
        st.dataframe(data_df)
else:
    with st.form("health_data_form"):
        st.write("Please enter the following health information:")

        age = st.number_input('Age', min_value=0, max_value=120, step=1)
        blood_pressure = st.number_input('Blood Pressure (mmHg)', min_value=80, max_value=200, step=1)
        cholesterol = st.number_input('Cholesterol (mg/dL)', min_value=100, max_value=400, step=1)
        diabetes = st.selectbox('Diabetes', ['No', 'Yes'])
        smoker = st.selectbox('Smoker', ['No', 'Yes'])
        bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, step=0.1)

        submitted = st.form_submit_button("Submit")
        if submitted:
            data = {
                "id": str(uuid4()),
                "age": age,
                "blood_pressure": blood_pressure,
                "cholesterol": cholesterol,
                "diabetes": 1 if diabetes == 'Yes' else 0,
                "smoker": 1 if smoker == 'Yes' else 0,
                "bmi": bmi
            }

            # Predict the hospitalization
            prediction = predict_hospitalization(data)

            if prediction:
                st.write("Based on the provided data, there's a higher risk of hospitalization.")
            else:
                st.write("Based on the provided data, there's a lower risk of hospitalization.")
