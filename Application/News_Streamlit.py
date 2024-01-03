import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment import SentimentIntensityAnalyzer
from streamlit_extras.mention import mention
import pickle
st.set_page_config(page_title="Topic & Sentiment Prediction of News Articles", page_icon="📰", layout="wide", initial_sidebar_state="auto")
# Load the TF-IDF vectorizer used during training
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Load the trained model from the file
with open('ovr_svm_classifier.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Initialize NLTK Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Create a function to get predictions
def predict_topic_sentiment(user_input):
    if user_input:
        # Transform user input using the loaded TF-IDF vectorizer
        text_vectorized = tfidf_vectorizer.transform([user_input])

        # Predict the topic using the loaded model
        predicted_topic = loaded_model.predict(text_vectorized)

        # Perform sentiment analysis on the user input
        sentiment_score = sia.polarity_scores(user_input)['compound']
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        col1, col2,col3 = st.columns(3)
        with col2:
            st.success(f"Predicted News Topic: 📰{predicted_topic[0]}")
            col4, col5, col6 = st.columns([2,6,2])
            with col5:
             st.markdown(
            f"""
            <style>
            .centered-content {{
                width: 250px;
                height: 250px;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                background-image: url('https://th.bing.com/th/id/R.8421c0b37230d4d57114b62ebcb994f9?rik=4f0t3HuCe2nWTw&riu=http%3a%2f%2ficon-park.com%2fimagefiles%2fnewspaper.png&ehk=7gnUb4vdJsO7I673kom96JpMO4Xe79hMbvXrhhJFyJI%3d&risl=&pid=ImgRaw&r=0');
                background-size: 100% 100%;
                box-shadow: 0px 0px 0px rgba(0, 1, 0, 1);
            }}

            .centered-content p {{
                font-size: 20px;  /* Reduced font size */
                font-weight: bold;
                font-style: italic;
                font-family: Spinaki;
                color: Black;
                margin: 0;  /* Remove default margin */
                text-align: center;
            }}
            </style>

            <div class="centered-content">
                <p>{predicted_topic[0]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
            if sentiment == "Positive":
                st.success(f"Sentiment: 😃{sentiment}")
            elif sentiment == "Negative":
                st.error(f"Sentiment: 😔{sentiment}")
            col7, col8, col9 = st.columns(3)
            with col9: 
               mention(
                    label="Vengatesan K",
                    icon="streamlit",
                    url="https://extras.streamlitapp.com",
                )
        
    else:
        st.warning("Please enter text.")

# Streamlit GUI
st.title("🗞️Topic & Sentiment Prediction of News Articles")
user_input = st.text_input("Enter News Text:", key='user_input')
if st.button("Predict Topic & Sentiment"):
    predict_topic_sentiment(user_input)
