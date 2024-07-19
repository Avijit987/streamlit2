import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # Replace with your model type
import pickle
# Load the trained model from the pickle file
model = pickle.load(open('house_price_prediction_model.pkl', 'rb'))

def main():
    """
    Streamlit app for house price prediction
    """

    # Title and description
    st.title('House Price Prediction App')
    st.write('Enter details about your house to predict its price.')

    # Input fields for house features
     sqft = st.number_input('Square Footage', min_value=0)
     bedrooms = st.number_input('Number of Bedrooms', min_value=0)
     bathrooms = st.number_input('Number of Bathrooms', min_value=0)  # Add more fields as needed

    # Create a DataFrame from user input (replace with your feature names)
    data = pd.DataFrame({
        'sqft': [sqft],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms]
    })

    # Prediction button
    if st.button('Predict Price'):
        # Preprocess the data if necessary (e.g., handle categorical features)
        # You might need to scale or encode features depending on your model

        prediction = model.predict(data)[0]

        # Display the prediction
        st.write(f'Predicted Price: ${prediction:,.2f}')

if __name__ == '__main__':
    main()
