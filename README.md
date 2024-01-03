# NewsClassifier
Building an Automated News Classification System with NLP Techniques
<hr>
<img align="left" alt="coding" width="480" height="250" src="https://techcrunch.com/wp-content/uploads/2022/08/signal-newsletter-india.jpg" />
<img align="right" alt="coding" width="480" height="250" src="https://krakensystems.co/assets/images/uploads/2018-09-17-figure1.png" />
<hr/>


## Context
Building a news classification system involves several steps, including web scraping, data
preprocessing, and model training.
***

## Steps Involved: 
1. **Web Scraping**
- Choosed news websites BBC, The Hindu, Times Now and CNN and used web scraping
tools or libraries BeautifulSoup to extract news articles.
- Retrieved the title and content of each news article. Ensured that have a diverse dataset
covering various topics.

2. **Data Cleaning and Preprocessing**
- Removed all irrelevant information, such as HTML tags, advertisements, or non-text content.
- Tokenized the text (split it into words or subwords) and removed stop words.
- Performed lemmatization or stemming to reduce words to their base form.
- Handled missing data and ensured a consistent format.
3. **Text Representation**
- Converted the text data into numerical format suitable for machine learning models. This can
be done using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) and word
embeddings GloVe.
- Used pre-trained word embeddings for better performance.
4. **Topic Clustering**
- Applied clustering algorithms K-means on the preprocessed text data to group similar articles together.
- Choosed the number of clusters based on the topics you want to identify Global, Entertainment, Politics, Sports.
5. **Topic Labeling**
- Manually inspected a sample of articles in each cluster to assign topic labels. This step helps in
labeling the clusters with meaningful topics.
6. **Classification Model**
- Splitted the data into training and testing sets.
- Trained a supervised machine learning model (e.g., Naive Bayes, Support Vector Machines, or deep learning models like LSTM or BERT) to predict the topic of a news article.
- Use the labeled clusters as ground truth labels for training the model.
7. **Evaluation**
- Evaluated the performance of your classification model on the testing set using appropriate metrics (accuracy, precision, recall, F1-score).
- Fine-tuned the model parameters if needed to improve performance.
8. **Deployment**
- Deployed a classification application using Tkinter

***
### Evaluation Metrics
<img align="left" alt="coding" width="480" height="280" src="https://github.com/Vengatesan-K/Iris-Species/assets/128688827/d37653ed-9e4d-4f35-91dc-33d30e8c354b" />
<img align="right" alt="coding" width="480" height="280" src="https://github.com/Vengatesan-K/Iris-Species/assets/128688827/3b41e587-77f6-4462-9d62-f7653f2dc022" />


## News Classification System Interface
<img alt="coding" src="https://github.com/Vengatesan-K/Python-Assessment/assets/128688827/bd8926ec-a9d9-4d92-a462-2c6cc993d40e" />
