# NewsClassifier

Building an Automated News Classification System with NLP Techniques

---

**Application/Web Link to Classify News Topic & Sentiment : [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vengat-newsclassifier-yncxskbpoprcqnjaijcxma.streamlit.app/)**

---

<div style="display: flex; justify-content: space-between;">
    <img src="https://techcrunch.com/wp-content/uploads/2022/08/signal-newsletter-india.jpg" alt="Coding" width="410" height="250" />
    <img src="https://krakensystems.co/assets/images/uploads/2018-09-17-figure1.png" alt="Coding" width="410" height="250" />
</div>

---


## Context

Building a news classification system involves several steps, including web scraping, data preprocessing, and model training.

---

## Steps Involved

1. **Web Scraping**
    - Selected news websites such as **BBC, The Hindu, Times Now, TOI and CNN** and utilized web scraping tools or libraries like BeautifulSoup to extract news articles.
    - Retrieved the title and content of each news article, ensuring a diverse dataset covering various topics.
    - **[https://github.com/News%20Scraping]("https://github.com/Vengatesan-K/NewsClassifier/blob/main/News%20Scraping/News_Scraping.ipynb")**
2. **Data Cleaning and Preprocessing**
    - Removed all irrelevant information, such as HTML tags, advertisements, or non-text content.
    - Tokenized the text (split it into words or subwords) and removed stop words.
    - Performed lemmatization or stemming to reduce words to their base form.
    - Handled missing data and ensured a consistent format.

3. **Text Representation**
    - Converted the text data into numerical format suitable for machine learning models, using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) and word embeddings GloVe.
    - Utilized pre-trained word embeddings for improved performance.

4. **Topic Clustering**
    - Applied clustering algorithms like K-means on the preprocessed text data to group similar articles together.
    - Determined the number of clusters based on desired topics such as Global, Entertainment, Politics, and Sports.

5. **Topic Labeling**
    - Manually inspected a sample of articles in each cluster to assign topic labels, facilitating meaningful topic labeling for the clusters.

6. **Classification Model**
    - Split the data into training and testing sets.
    - Trained a supervised machine learning model (e.g., Naive Bayes, Support Vector Machines, or deep learning models like LSTM or BERT) to predict the topic of a news article.
    - Used the labeled clusters as ground truth labels for training the model.

7. **Evaluation**
    - Assessed the performance of the classification model on the testing set using appropriate metrics (accuracy, precision, recall, F1-score).
    - Fine-tuned the model parameters as needed to enhance performance.

8. **Deployment**
    - Deployed a classification application using Tkinter.

---

### Evaluation Metrics

![Coding](https://github.com/Vengatesan-K/Iris-Species/assets/128688827/d37653ed-9e4d-4f35-91dc-33d30e8c354b)

<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Vengatesan-K/Iris-Species/assets/128688827/3b41e587-77f6-4462-9d62-f7653f2dc022" alt="Coding" width="410" height="250" />
    <img src="https://github.com/Vengatesan-K/Iris-Species/assets/128688827/24b2f531-5c49-417c-891c-053694f09112" width="410" height="250" />
</div>

---

## News Classification System Interfaces :

### Tkinter's Interface:

![Coding](https://github.com/Vengatesan-K/Python-Assessment/assets/128688827/bd8926ec-a9d9-4d92-a462-2c6cc993d40e)

### Streamlit Interface :

![Screenshot 2024-01-03 165840](https://github.com/Vengatesan-K/IMDB-Movies-Analysis/assets/128688827/fc0ec77c-9d0a-487f-91c9-cdaba7b3c031)
