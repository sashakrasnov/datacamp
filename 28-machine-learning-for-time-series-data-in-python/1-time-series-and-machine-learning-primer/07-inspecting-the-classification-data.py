'''
Inspecting the classification data

In these final exercises of this chapter, you'll explore the two datasets you'll use in this course.

The first is a collection of heartbeat sounds. Hearts normally have a predictable sound pattern as they beat, but some disorders can cause the heart to beat abnormally. This dataset contains a training set with labels for each type of heartbeat, and a testing set with no labels. You'll use the testing set to validate your models.

As you have labeled data, this dataset is ideal for classification. In fact, it was originally offered as a part of a public Kaggle competition (https://www.kaggle.com/kinguistics/heartbeat-sounds).
'''

import numpy as np
import matplotlib.pyplot as plt

data_dir = '../datasets'

'''
INSTRUCTIONS

*   Use glob to return a list of the .wav files in data_dir directory.
*   Import the first audio file using librosa.
*   Generate a time array for the data.
*   Plot the waveform for this file, along with the time array.
'''

import librosa as lr
from glob import glob

# List all the wav files in the folder
audio_files = glob(data_dir + '/*.wav')

# Read in the first audio file, create the time array
audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq

# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()
