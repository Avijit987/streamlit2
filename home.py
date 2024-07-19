import streamlit as st


st.title("House Price Prediction App")

# Import your machine learning model from model.py
from model import load_model, make_prediction

# Title and description for your app
st.write("Enter the area to get a prediction price.")

# User input elements based on your model's features
# Example: numeric input for a house price prediction model
sqft = st.number_input("Area:", min_value=0)

# Button to trigger prediction
if st.button("Predict"):
    # Load your model (if not already loaded)
    model = load_model()

    # Prepare user input data (might involve conversion or reshaping)
    input_data = [[ sqft]]

    # Make prediction using the model
    prediction = make_prediction(model, input_data)

    # Display the prediction result
    st.write("Predicted value:", prediction)

