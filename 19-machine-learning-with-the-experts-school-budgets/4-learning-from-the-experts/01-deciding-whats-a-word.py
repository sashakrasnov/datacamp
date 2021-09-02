'''
Deciding what's a word

Before you build up to the winning pipeline, it will be useful to look a little deeper into how the text features will be processed.

In this exercise, you will use CountVectorizer on the training data X_train (preloaded into the workspace) to see the effect of tokenization on punctuation.

Remember, since CountVectorizer expects a vector, you'll need to use the preloaded function, combine_text_columns before fitting to the training data.
'''

from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type', 'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']
NUMERIC_COLUMNS = ['FTE', 'Total']

# Define combine_text_columns()
def combine_text_columns(data_frame, to_drop=NUMERIC_COLUMNS + LABELS):
    """ converts all text in each row of data_frame to single vector """
    
    # Drop non-text columns that are in the df
    to_drop = set(to_drop) & set(data_frame.columns.tolist())
    text_data = data_frame.drop(to_drop, axis=1)
    
    # Replace nans with blanks
    text_data.fillna("", inplace=True)
    
    # Join all text items in a row that have a space in between
    return text_data.apply(lambda x: " ".join(x), axis=1)


df = pd.read_csv('../datasets/school-budgets.csv', index_col=0).loc[:, 'Object_Description':]

X_train, X_test = train_test_split(df, test_size=0.2, random_state=123)

'''
INSTRUCTIONS

*   Create text_vector by preprocessing X_train using combine_text_columns. This is important, or else you won't get any tokens!
*   Instantiate CountVectorizer as text_features. Specify the keyword argument token_pattern=TOKENS_ALPHANUMERIC.
*   Fit text_features to the text_vector.
*   Hit 'Submit Answer' to print the first 10 tokens.
'''

# Import the CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create the text vector
text_vector = combine_text_columns(X_train)

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# Instantiate the CountVectorizer: text_features
text_features = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

# Fit text_features to the text vector
text_features.fit(text_vector)

# Print the first 10 tokens
print(text_features.get_feature_names()[:10])
