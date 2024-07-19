import pickle  # Assuming you're using pickle to save your model


# Function to load your saved model
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# Function to make predictions using the loaded model
def make_prediction(model, data):
    # Preprocess data if necessary (e.g., scaling)
    # Make predictions using the model
    predictions = model.predict(data)
    return predictions[0]  # Assuming single prediction output
