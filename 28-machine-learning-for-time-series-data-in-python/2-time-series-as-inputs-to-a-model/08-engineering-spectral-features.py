'''
Engineering spectral features

As you can probably tell, there is a lot more information in a spectrogram compared to a raw audio file. By computing the spectral features, you have a much better idea of what's going on. As such, there are all kinds of spectral features that you can compute using the spectrogram as a base. In this exercise, you'll look at a few of these features.

The spectogram spec from the previous exercise is available in your workspace.
'''

import numpy as np
import matplotlib.pyplot as plt

from librosa.core import stft

sfreq = 2205
HOP_LENGTH = 2**4

audio = np.loadtxt('../datasets/heartbeats_abnormal.csv', delimiter=',', skiprows=1, usecols=[1])

spec = np.abs(stft(audio, hop_length=HOP_LENGTH, n_fft=2**7))

times_spec = np.linspace(0, sfreq/spec.shape[1], spec.shape[1])

'''
INSTRUCTIONS 1/2

*   Calculate the spectral bandwidth as well as the spectral centroid of the spectrogram by using functions in librosa.feature.
'''

import librosa as lr

# Calculate the spectral centroid and bandwidth for the spectrogram
bandwidths = lr.feature.spectral_bandwidth(S=spec)[0]
centroids = lr.feature.spectral_centroid(S=spec)[0]

'''
INSTRUCTIONS 2/2

*   Convert the spectrogram to decibels for visualization.
*   Plot the spectrogram over time.
'''

from librosa.core import amplitude_to_db
from librosa.display import specshow

# Convert spectrogram to decibels for visualization
spec_db = amplitude_to_db(spec)

# Display these features on top of the spectrogram
fig, ax = plt.subplots(figsize=(10, 5))
ax = specshow(spec_db, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH)
ax.plot(times_spec, centroids)
ax.fill_between(times_spec, centroids - bandwidths / 2, centroids + bandwidths / 2, alpha=.5)
ax.set(ylim=[None, 6000])
plt.show()
