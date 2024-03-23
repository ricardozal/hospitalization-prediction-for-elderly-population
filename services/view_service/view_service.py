import streamlit as st
import pandas as pd
from uuid import uuid4
from gateway import predict_hospitalization, predict_hospitalization_bunch
from common.settings import MODEL_VARIABLES

data = dict()


def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error processing file: {e}")
            return None
    return None


if __name__ == "__main__":
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

            for key in MODEL_VARIABLES.keys():
                description = MODEL_VARIABLES[key]["description"]
                if MODEL_VARIABLES[key]["is_categorical"]:
                    options = MODEL_VARIABLES[key]["values"].keys()
                    data[key] = st.selectbox(description, options)
                elif MODEL_VARIABLES[key]["type"] == "float":
                    data[key] = st.number_input(
                        description, min_value=0., step=1.)
                else:
                    data[key] = st.number_input(
                        description,
                        min_value=MODEL_VARIABLES[key]["min_value"],
                        max_value=MODEL_VARIABLES[key]["max_value"],
                        step=1)

            submitted = st.form_submit_button("Submit")
            if submitted:
                # Predict the hospitalization
                data["id"] = str(uuid4())
                prediction, score = predict_hospitalization(data)

                if prediction:
                    st.write("Based on the provided data, there's a higher risk of hospitalization.")
                    st.write(f"Probability: {score * 100}%")
                else:
                    st.write("Based on the provided data, there's a lower risk of hospitalization.")
