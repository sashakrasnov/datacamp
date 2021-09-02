'''
Calculating features from the envelope

Now that you've removed some of the noisier fluctuations in the audio, let's see if this improves your ability to classify.

audio_rectified_smooth from the previous exercise is available in your workspace.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import LinearSVC

normal = pd.read_csv('../datasets/heartbeats_normal_full.csv', index_col=0)
abnormal = pd.read_csv('../datasets/heartbeats_abnormal_full.csv', index_col=0)

labels = np.array(['normal'] * len(normal.columns) + ['abnormal'] * len(abnormal.columns))
audio = pd.concat([normal, abnormal], axis=1)

audio_rectified = audio.apply(np.abs)
audio_rectified_smooth = audio_rectified.rolling(50).mean()

model = LinearSVC()

'''
INSTRUCTIONS

*   Calculate the mean, standard deviation, and maximum value for each heartbeat sound.
*   Column stack these stats in the same order.
*   Use cross-validation to fit a model on each CV iteration.
'''

# Calculate stats
means = np.mean(audio_rectified_smooth, axis=0)
stds = np.std(audio_rectified_smooth, axis=0)
maxs = np.max(audio_rectified_smooth, axis=0)

# Create the X and y arrays
X = np.column_stack([means, stds, maxs])
y = labels#.reshape([-1, 1])

# Fit the model and score on testing data
from sklearn.model_selection import cross_val_score
percent_score = cross_val_score(model, X, y, cv=5)
print(np.mean(percent_score))