import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("model.pkl")
countvec = joblib.load("countvec.pkl")

# App title
st.title("📈 Stock Price Prediction App")

# Input from user
user_input = st.text_area("Enter stock-related text (e.g., news, tweets, headlines):")

# Predict button
if st.button("Predict"):
    if user_input.strip():
        # Transform the input
        transformed = countvec.transform([user_input])
        
        # Predict
        prediction = model.predict(transformed)[0]
        
        st.success(f"Predicted Stock Movement: {prediction}")
    else:
        st.warning("⚠️ Please enter some text before predicting.")
