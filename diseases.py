# diseases.py

import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

def run_disease_app():
    # Load your model
    with open(r'C:\Users\Acer\Downloads\model1.pkl', 'rb') as file:
        classifierDT = pickle.load(file)

    # List of symptoms (features)
    symptom_names = [
        'itching', 'skin_rash', 'continuous_sneezing', 'chills', 'vomiting',
        'fatigue', 'cough', 'high_fever', 'headache', 'yellowish_skin',
        'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'abdominal_pain',
        'diarrhoea', 'mild_fever', 'yellowing_of_eyes', 'malaise', 'throat_irritation',
        'chest_pain', 'pain_in_anal_region', 'neck_pain', 'muscle_weakness',
        'loss_of_balance', 'bladder_discomfort', 'irritability', 'muscle_pain',
        'polyuria', 'receiving_unsterile_injections', 'coma', 'palpitations',
        'painful_walking', 'yellow_crust_ooze'
    ]

    # User input for symptoms
    st.title("Disease Prediction Based on Symptoms")

    # Display symptoms in rows with checkboxes
    selected_symptoms = []
    num_columns = 3  # Number of symptoms per row

    # Create columns for symptoms
    cols = st.columns(num_columns)

    for i, symptom in enumerate(symptom_names):
        col_index = i % num_columns
        if cols[col_index].checkbox(symptom):
            selected_symptoms.append(1)  # Symptom present
        else:
            selected_symptoms.append(0)  # Symptom absent

    # Convert to numpy array for prediction
    newdata = [selected_symptoms]

    # Prediction button
    if st.button("Predict Disease"):
        if sum(selected_symptoms) == 0:
            st.write("Please select at least one symptom to predict a disease.")
        else:
            probaDT = classifierDT.predict_proba(newdata)
            predDT = classifierDT.predict(newdata)
            st.write("Predicted Disease:", predDT[0])

            # Probability distribution
            probabilities = probaDT[0]
            class_names = classifierDT.classes_

            # Create a bar chart
            st.write("Probability Distribution:")
            st.bar_chart(probabilities)

            # Alternatively, create a matplotlib bar chart
            plt.figure(figsize=(10, 5))
            plt.bar(class_names, probabilities, color='skyblue')
            plt.xlabel('Diseases')
            plt.ylabel('Probability')
            plt.title('Probability Distribution of Predicted Diseases')
            plt.xticks(rotation=90, ha='right')
            plt.tight_layout()

            # Display the matplotlib chart in Streamlit
            st.pyplot(plt)
