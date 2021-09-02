'''
Combining many features in a classifier

You've spent this lesson engineering many features from the audio data - some contain information about how the audio changes in time, others contain information about the spectral content that is present.

The beauty of machine learning is that it can handle all of these features at the same time. If there is different information present in each feature, it should improve the classifier's ability to distinguish the types of audio. Note that this often requires more advanced techniques such as regularization, which we'll cover in the next chapter.

For the final exercise in the chapter, we've loaded many of the features that you calculated before. Combine all of them into an array that can be fed into the classifier, and see how it does.
'''

import numpy as np
import librosa as lr
import matplotlib.pyplot as plt

from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

sfreq = 2205

spectrograms = np.loadtxt('../datasets/spectrograms.csv', delimiter=',').reshape((60,65,552))
labels = np.array(['normal', 'normal', 'normal', 'murmur', 'normal', 'normal',
                   'normal', 'murmur', 'normal', 'murmur', 'normal', 'normal',
                   'normal', 'murmur', 'murmur', 'normal', 'normal', 'murmur',
                   'murmur', 'normal', 'murmur', 'murmur', 'murmur', 'murmur',
                   'normal', 'normal', 'murmur', 'normal', 'normal', 'murmur',
                   'murmur', 'murmur', 'murmur', 'murmur', 'murmur', 'normal',
                   'normal', 'murmur', 'murmur', 'murmur', 'normal', 'murmur',
                   'murmur', 'normal', 'normal', 'normal', 'murmur', 'murmur',
                   'murmur', 'normal', 'normal', 'normal', 'normal', 'murmur',
                   'normal', 'normal', 'murmur', 'murmur', 'murmur', 'murmur'])

model = LinearSVC()

means = []
stds = []
maxs = []
tempo_mean = []
tempo_std = []
tempo_max = []

for spec in spectrograms:
    means.append(spec.mean())
    stds.append(spec.std())
    maxs.append(spec.max())

    shape = spec.shape[0] * spec.shape[1]
    tempo_mean.append(lr.beat.tempo(spec.reshape(shape), hop_length=spec.shape[1], aggregate=None).mean())
    tempo_std.append(lr.beat.tempo(spec.reshape(shape), hop_length=spec.shape[1], aggregate=None).std())
    tempo_max.append(lr.beat.tempo(spec.reshape(shape), hop_length=spec.shape[1], aggregate=None).max())

'''
INSTRUCTIONS 1/2

*   Loop through each spectrogram, calculating the mean spectral bandwidth and centroid of each.
'''

# Loop through each spectrogram
bandwidths = []
centroids = []

for spec in spectrograms:
    # Calculate the mean spectral bandwidth
    this_mean_bandwidth = np.mean(lr.feature.spectral_bandwidth(S=spec))
    # Calculate the mean spectral centroid
    this_mean_centroid = np.mean(lr.feature.spectral_centroid(S=spec))
    # Collect the values
    bandwidths.append(this_mean_bandwidth)  
    centroids.append(this_mean_centroid)

'''
INSTRUCTIONS 2/2

*   Column stack all the features to create the array X.
*   Score the classifier with cross-validation.
'''

# Create X and y arrays
X = np.column_stack([means, stds, maxs, tempo_mean, tempo_max, tempo_std, bandwidths, centroids])
y = labels.reshape([-1, 1])

# Fit the model and score on testing data
percent_score = cross_val_score(model, X, y, cv=5)
print(np.mean(percent_score))