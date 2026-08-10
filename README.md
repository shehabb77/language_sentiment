# 😊 Transformer Sentiment Analyzer

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url-goes-here.streamlit.app)

## Overview
This web application performs real-time sentiment analysis using a pre-trained state-of-the-art AI model. It takes user text as input and instantly predicts whether the underlying emotion is **Positive**, **Neutral**, or **Negative**, providing a detailed confidence percentage for each category via a clean visual interface.

This project was developed and deployed as part of the NTI Online Summer Internship (Machine Learning Track).

## Technologies Used
* **Python:** The core programming language.
* **Streamlit:** Used to build the interactive web frontend and handle cloud deployment.
* **PyTorch:** The underlying deep learning mathematical framework used for model inference.
* **Hugging Face Transformers:** Used to access and implement the `twitter-roberta-base-sentiment-latest` model.

## How It Works
The application utilizes a RoBERTa-base transformer model that has been specifically fine-tuned on millions of Twitter/X posts. Because it was trained on social media data, the model is highly capable of understanding informal language, slang, and context compared to older, traditional sentiment analysis methods. 

## How to Run Locally
If you want to run this project on your own machine, follow these beginner-friendly steps:

1. **Clone the repository:**
   Open your terminal or command prompt and run:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
