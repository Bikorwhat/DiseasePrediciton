
import streamlit as st
from diabitites import run_diabetes_app  # Import the function from diabitites.py
from diseases import run_disease_app  # Import the function from diseases.py
from kidney import run_kidney_app  # Import the function from kidney.py

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Function to switch pages
def navigate_to_page(page_name):
    st.session_state['page'] = page_name

# Main app layout
st.title("Health Checker")

# Home Page Layout
if st.session_state['page'] == 'home':
    # Check Disease Button (Redirects to diseases.py)
    if st.button("Check Disease"):
        navigate_to_page('disease')

    # Dropdown for Specific Disease
    st.subheader("Check Specific Disease")
    disease_option = st.selectbox(
        "Select a Disease to Check",
        ("Diabetes", "Kidney")
    )

    # Button to navigate to the specific disease page
    if st.button(f"Check {disease_option}"):
        navigate_to_page(disease_option.lower())

# Disease Prediction Page (from diseases.py)
elif st.session_state['page'] == 'disease':
    run_disease_app()  # Call the function from diseases.py
    st.button("Go Back", on_click=lambda: navigate_to_page('home'))

# Diabetes Prediction Page (from diabitites.py)
elif st.session_state['page'] == 'diabetes':
    run_diabetes_app()  # Call the function from diabitites.py
    st.button("Go Back", on_click=lambda: navigate_to_page('home'))


elif st.session_state['page'] == 'kidney':
    run_kidney_app()
    st.button("Go Back", on_click=lambda: navigate_to_page('home'))
