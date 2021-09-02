'''
Sentiment analysis for movie reviews

In this exercise you'll explore the probabilities outputted by logistic regression on a subset of the Large Movie Review Dataset - http://ai.stanford.edu/~amaas/data/sentiment/. The variables X and y are already loaded into the environment. X contains features based on the number of times words appear in the movie reviews, and y contains labels for whether the review sentiment is positive (+1) or negative (-1).
'''

from sklearn.feature_extraction.text import CountVectorizer
import scipy.sparse as sps
from sklearn.linear_model import LogisticRegression

def get_features(review):
    return vectorizer.transform([review])

with open('../datasets/imdb.vocab') as f:
    imdb_voc = [f.readline().strip() for _ in range(2500)]

vectorizer = CountVectorizer(vocabulary=imdb_voc)

X = sps.load_npz('../datasets/X_train.csr.npz')
y = sps.load_npz('../datasets/y_train.csr.npz').data

'''
INSTRUCTIONS

*   Train a logistic regression model on the movie review data.
*   Predict the probabilities of negative vs. positive for the two given reviews.
*   Feel free to write your own reviews and get probabilities for those too!
'''

# Instantiate logistic regression and train
lr = LogisticRegression()
lr.fit(X, y)

# Predict sentiment for a glowing review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Review:", review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])

# Predict sentiment for a poor review
review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
review2_features = get_features(review2)
print("Review:", review2)
print("Probability of positive review:", lr.predict_proba(review2_features)[0,1])