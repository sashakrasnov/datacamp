'''
Derivative features: The tempogram

One benefit of cleaning up your data is that it lets you compute more sophisticated features. For example, the envelope calculation you performed is a common technique in computing tempo and rhythm features. In this exercise, you'll use librosa to compute some tempo and rhythm features for heartbeat data, and fit a model once more.

Note that librosa functions tend to only operate on numpy arrays instead of DataFrames, so we'll access our Pandas data as a Numpy array with the .values attribute.
'''

import numpy as np
import pandas as pd
import librosa as lr

from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

normal = pd.read_csv('../datasets/heartbeats_normal_full.csv', index_col=0)
abnormal = pd.read_csv('../datasets/heartbeats_abnormal_full.csv', index_col=0)

labels = np.array(['normal'] * len(normal.columns) + ['abnormal'] * len(abnormal.columns))
audio = pd.concat([normal, abnormal], axis=1)

audio.columns = list(range(len(audio.columns)))

sfreq = 2205

audio_rectified = audio.apply(np.abs)
audio_rectified_smooth = audio_rectified.rolling(50).mean()

means = np.mean(audio_rectified_smooth, axis=0)
stds = np.std(audio_rectified_smooth, axis=0)
maxs = np.max(audio_rectified_smooth, axis=0)

model = LinearSVC()

'''
INSTRUCTIONS 1/2

*   Use librosa to calculate a tempogram of each heartbeat audio.
*   Calculate the mean, standard deviation, and maximum of each tempogram (this time using DataFrame methods)
'''

# Calculate the tempo of the sounds
tempos = []
for col, i_audio in audio.items():
    tempos.append(lr.beat.tempo(i_audio.values, sr=sfreq, hop_length=2**6, aggregate=None))

# Convert the list to an array so you can manipulate it more easily
tempos = np.array(tempos)

# Calculate statistics of each tempo
tempos_mean = tempos.mean(axis=-1)
tempos_std = tempos.std(axis=-1)
tempos_max = tempos.max(axis=-1)

'''
INSTRUCTIONS 2/2

*   Column stack these features (mean, standard deviation, and maximum) in the same order.
*   Score the classifier with cross-validation.
'''

# Create the X and y arrays
X = np.column_stack([means, stds, maxs, tempos_mean, tempos_std, tempos_max])
y = labels.reshape([-1, 1])

# Fit the model and score on testing data
percent_score = cross_val_score(model, X, y, cv=5)
print(np.mean(percent_score))