import streamlit as st
import pandas as pd
from utils import predict_stroke, preprocess_data

st.set_page_config(layout='wide')

st.title('Wanna See if you might have stroke?')

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    age = st.number_input('Enter your age')
    hypertension = st.radio(
        "Hypertension",
        ("Yes", "No")
    )
    heart_disease = st.radio(
        "Heart Disease",
        ("Yes", "No")
    )

hypertension = 1 if hypertension == 'Yes' else 0
heart_disease = 1 if heart_disease == 'Yes' else 0

with col2:
    ever_married = st.radio(
        "Ever Married",
        ("Yes", "No")
    )
    avg_glucose_level = st.number_input(label='Average Glucose Level')
    smoking_status = st.radio(
        "Smoking Status",
        ("Formerly Smoked", "Smokes", "Never Smoked", "Unknown")
    )

btn_clicked = st.button(
    label="Predict", 
    key="predictBtn"
  )

ever_married = 1 if ever_married == 'Yes' else 0

if smoking_status == 'Formerly Smoked':
    smoking_status = 0
elif smoking_status == 'Never Smoked':
    smoking_status = 1
elif smoking_status == 'Smokes':
    smoking_status = 2
else:
    smoking_status = 3
    

input_data = {
    'age': age, 
    'hypertension': hypertension,
    'heart_disease': heart_disease,
    'ever_married': ever_married,
    'avg_glucose_level': avg_glucose_level,
    'smoking_status': smoking_status
    }

df = pd.DataFrame(data=input_data, index=[0])

proccessed_data = preprocess_data(df)

if btn_clicked:
    result = predict_stroke(proccessed_data)

    if result == 0:
        st.write('There is less chance you will have stroke')
    else:
        st.write('There is high chance of getting stroke')
