'''
Spectrograms of heartbeat audio

Spectral engineering is one of the most common techniques in machine learning for time series data. The first step in this process is to calculate a spectrogram of sound. This describes what spectral content (e.g., low and high pitches) are present in the sound over time. In this exercise, you'll calculate a spectrogram of a heartbeat audio file.

We've loaded a single heartbeat sound in the variable audio.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sfreq = 2205

audio = np.loadtxt('../datasets/heartbeats_abnormal.csv', delimiter=',', skiprows=1, usecols=1)
time = np.arange(0, len(audio)) / sfreq

'''
INSTRUCTIONS 1/2

*   Import the short-time fourier transform (stft) function from librosa.core.
*   Calculate the spectral content (using the short-time fourier transform function) of audio.
'''

# Import the stft function
from librosa.core import stft

# Prepare the STFT
HOP_LENGTH = 2**4
spec = stft(audio, hop_length=HOP_LENGTH, n_fft=2**7)

'''
INSTRUCTIONS 2/2

*   Convert the spectogram (spec) to decibels.
*   Visualize the spectogram.
'''

from librosa.core import amplitude_to_db
from librosa.display import specshow

# Convert into decibels
spec_db = amplitude_to_db(spec)

# Compare the raw audio to the spectrogram of the audio
fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
axs[0].plot(time, audio)
specshow(spec_db, sr=sfreq, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH)
plt.show()