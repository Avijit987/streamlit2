import streamlit as st
from model import load_model, make_prediction  # Import your model functions

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# Title and description
st.title("House Price Prediction App")
st.write(
    """
    Enter the area in square feet to get a prediction price.
    """
)

# User input elements
sqft_container = st.container()  # Create a container for visual styling
with sqft_container:
    col1, col2 = st.columns(2)  # Create two columns for responsive layout
    with col1:
        sqft = st.number_input("Area (sqft):", min_value=0, key="area_input")  # Use a unique key for consistent updates
    with col2:
        st.write("**(in square feet)**")  # Clarify input unit

# Button to trigger prediction
if st.button("Predict"):
    try:
        # Load the model (if not already loaded)
        model = load_model()

        # Prepare user input data (might involve conversion or reshaping)
        input_data = [[sqft]]

        # Make prediction using the model
        prediction = make_prediction(model, input_data)

        # Display the prediction result with formatting
        st.success(f"Predicted value: ${prediction:.2f}")  # Format prediction with decimals and dollar sign

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")  # Handle errors more informatively
