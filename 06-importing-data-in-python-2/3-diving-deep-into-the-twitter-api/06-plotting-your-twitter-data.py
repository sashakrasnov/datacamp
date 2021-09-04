'''
Plotting your Twitter data

Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data. You'll use the statistical data visualization library seaborn, which you may not have seen before, but we'll guide you through. You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot, passing it two arguments:

*   a list of labels and
*   a list containing the variables you wish to plot (clinton, trump and so on.)

Hopefully, you'll see that Trump was unreasonably represented! We have already run the previous exercise solutions in your environment.
'''

import json
import pandas as pd
import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True

    return False


tweets_data_path = '../datasets/tweets3.txt'

tweets_data = []

with open(tweets_data_path, 'r') as tweets_file:
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

'''
Instructions

*   Import both matplotlib.pyplot and seaborn using the aliases plt and sns, respectively.
*   Complete the arguments of sns.barplot: the first argument should be the labels to appear on the x-axis; the second argument should be the list of the variables you wish to plot, as produced in the previous exercise.
'''

# Import packages
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(x=cd, y=[clinton, trump, sanders, cruz])
ax.set(ylabel='count')
plt.show()
