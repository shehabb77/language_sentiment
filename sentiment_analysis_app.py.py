import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Caching the model
# We use @st.cache_resource so the large model only loads once, 
# rather than downloading/reloading every time the user clicks "Predict".
@st.cache_resource
def load_model():
    MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()
labels = ["Negative 😠", "Neutral 😐", "Positive 😊"]

# 2. The prediction function (same logic as your notebook)
def predict_sentiment(text):
    if len(text.strip()) == 0:
        return None
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = torch.softmax(outputs.logits, dim=1)[0]
    return {labels[0]: float(probs[0]), labels[1]: float(probs[1]), labels[2]: float(probs[2])}

# 3. Building the User Interface
st.title("😊 Transformer Sentiment Analyzer")
st.write("Enter any sentence and the Transformer model will predict whether it is Positive, Neutral, or Negative.")

# Create a text box for the user
user_text = st.text_area("Type your sentence here...")

# Create a button to trigger the prediction
if st.button("Predict"):
    if user_text:
        with st.spinner("Analyzing..."):
            results = predict_sentiment(user_text)
            st.write(results)
    else:
        st.warning("Please enter some text.")