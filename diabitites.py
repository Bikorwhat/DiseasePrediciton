# diabetes.py

import streamlit as st
import pandas as pd
import joblib

def run_diabetes_app():
    # Load the trained model
    model = joblib.load(r'C:\Users\Acer\Downloads\diabities.pkl')

    # Define the app
    st.title('Diabetes Prediction App')

    # Input fields for user
    pregnancies = st.number_input('Pregnancies', min_value=0)
    glucose = st.number_input('Glucose', min_value=0)
    blood_pressure = st.number_input('Blood Pressure', min_value=0)
    skin_thickness = st.number_input('Skin Thickness', min_value=0)
    insulin = st.number_input('Insulin', min_value=0)
    bmi = st.number_input('BMI', min_value=0.0)
    pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    age = st.number_input('Age', min_value=0)

    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree_function, age]],
                              columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    # Predict
    if st.button('Predict'):
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.write('The model predicts that you have diabetes.')
        else:
            st.write('The model predicts that you do not have diabetes.')
