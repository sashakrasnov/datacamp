'''
Clustering Wikipedia part II

It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.

A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline chaining TruncatedSVD with KMeans is available.
'''

from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

titles = [
    'HTTP 404',
    'Alexa Internet',
    'Internet Explorer',
    'HTTP cookie',
    'Google Search',
    'Tumblr',
    'Hypertext Transfer Protocol',
    'Social search',
    'Firefox',
    'LinkedIn',
    'Global warming',
    'Nationally Appropriate Mitigation Action',
    'Nigel Lawson',
    'Connie Hedegaard',
    'Climate change',
    'Kyoto Protocol',
    '350.org',
    'Greenhouse gas emissions by the United States',
    '2010 United Nations Climate Change Conference',
    '2007 United Nations Climate Change Conference',
    'Angelina Jolie',
    'Michael Fassbender',
    'Denzel Washington',
    'Catherine Zeta-Jones',
    'Jessica Biel',
    'Russell Crowe',
    'Mila Kunis',
    'Dakota Fanning',
    'Anne Hathaway',
    'Jennifer Aniston',
    'France national football team',
    'Cristiano Ronaldo',
    'Arsenal F.C.',
    'Radamel Falcao',
    'Zlatan Ibrahimović',
    'Colombia national football team',
    '2014 FIFA World Cup qualification',
    'Football',
    'Neymar',
    'Franck Ribéry',
    'Tonsillitis',
    'Hepatitis B',
    'Doxycycline',
    'Leukemia',
    'Gout',
    'Hepatitis C',
    'Prednisone',
    'Fever',
    'Gabapentin',
    'Lymphoma',
    'Chad Kroeger',
    'Nate Ruess',
    'The Wanted',
    'Stevie Nicks',
    'Arctic Monkeys',
    'Black Sabbath',
    'Skrillex',
    'Red Hot Chili Peppers',
    'Sepsis',
    'Adam Levine']

svd = TruncatedSVD(n_components=50)

kmeans = KMeans(n_clusters=6)

pipeline = make_pipeline(svd, kmeans)

'''
INSTRUCTIONS

*   Import pandas as pd.
*   Fit the pipeline to the word-frequency array articles.
*   Predict the cluster labels.
*   Align the cluster labels with the list titles of article titles by creating a DataFrame df with labels and titles as columns. This has been done for you.
*   Use the .sort_values() method of df to sort the DataFrame by the 'label' column, and print the result.
*   Hit 'Submit Answer' and take a moment to investigate your amazing clustering of Wikipedia pages!
'''

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))
