import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load(r'C:\Users\Acer\Downloads\kidney2.pkl')

# Function to make predictions
def predict_kidney_disease(features):
    return model.predict([features])[0]

# Function to run the kidney disease prediction app
def run_kidney_app():
    st.title("Kidney Disease Prediction")

    st.markdown("""
    This application predicts the presence of kidney disease based on input medical parameters.
    Please enter the values for the following parameters:
    """)

    # Input fields for user inputs
    age = st.number_input("Age (e.g., 50)", min_value=0)
    bp = st.number_input("Blood Pressure (e.g., 80)", min_value=0)
    al = st.number_input("Albumin (e.g., 0)", min_value=0)
    su = st.number_input("Sugar (e.g., 0)", min_value=0)
    rbc = st.selectbox("Red Blood Cells", ("Normal", "Abnormal"))  
    pc = st.selectbox("Pus Cells", ("Normal", "Abnormal"))  
    pcc = st.selectbox("Pus Cell Clumps", ("Not Present", "Present"))  
    ba = st.selectbox("Bacteria", ("Not Present", "Present"))  
    bgr = st.number_input("Blood Glucose Random (e.g., 120)", min_value=0)
    bu = st.number_input("Blood Urea (e.g., 50)", min_value=0)
    sc = st.number_input("Serum Creatinine (e.g., 1.5)", min_value=0.0)
    wc = st.number_input("White Blood Cell Count (e.g., 6200)", min_value=0)
    pot = st.number_input("Potassium (e.g., 4)", min_value=0)  # Assuming additional input
    hypertension = st.selectbox("Hypertension", ("No", "Yes"))
    dm = st.selectbox("Diabetes Mellitus", ("No", "Yes"))
    cad = st.selectbox("Coronary Artery Disease", ("No", "Yes"))
    pe = st.selectbox("Edema", ("No", "Yes"))
    ane = st.selectbox("Anemia", ("No", "Yes"))

    # Convert categorical inputs to numerical values
    rbc = 1 if rbc == "Abnormal" else 0
    pc = 1 if pc == "Abnormal" else 0
    pcc = 1 if pcc == "Present" else 0
    ba = 1 if ba == "Present" else 0
    hypertension = 1 if hypertension == "Yes" else 0
    dm = 1 if dm == "Yes" else 0
    cad = 1 if cad == "Yes" else 0
    pe = 1 if pe == "Yes" else 0
    ane = 1 if ane == "Yes" else 0

    # Create a button to predict
    if st.button("Predict"):
        features = [age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot, wc, hypertension, dm, cad, pe, ane]
        prediction = predict_kidney_disease(features)

        # Display the result
        if prediction == 1:
            st.success("The patient is at risk of kidney disease.")
        else:
            st.success("The patient is not at risk of kidney disease.")
