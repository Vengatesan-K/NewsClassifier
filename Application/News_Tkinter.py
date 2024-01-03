import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment import SentimentIntensityAnalyzer
import pickle

# Load the TF-IDF vectorizer used during training
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Load the trained model from the file
with open('ovr_svm_classifier.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Initialize NLTK Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Create a function to get predictions
def predict_topic_sentiment():
    user_input = entry.get()  # Get text from the input field
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

        messagebox.showinfo("Prediction", f"Predicted Topic: {predicted_topic[0]}\nSentiment: {sentiment}")
    else:
        messagebox.showwarning("Warning", "Please enter text.")

# Create the GUI window
root = tk.Tk()
root.title("Topic & Sentiment Prediction of News Articles")

# Create input label and entry field
label = tk.Label(root, text="Enter Text:")
label.pack()
entry = tk.Entry(root, width=100, borderwidth=5, relief="sunken")
entry.focus_set()
entry.bind("<Return>", lambda event: predict_topic_sentiment())
entry.pack()

# Create a button to trigger prediction
predict_button = tk.Button(root, text="Predict Topic & Sentiment", command=predict_topic_sentiment)
predict_button.pack()

# Run the GUI application
root.mainloop()
