'''
Calculating the envelope of sound

One of the ways you can improve the features available to your model is to remove some of the noise present in the data. In audio data, a common way to do this is to smooth the data and then rectify it so that the total amount of sound energy over time is more distinguishable. You'll do this in the current exercise.

A heartbeat file is available in the variable audio.
'''

import numpy as np
import pandas as pd
import librosa as lr
import matplotlib.pyplot as plt

# Read in the first audio file, create the time array
data, sfreq = lr.load('../datasets/murmur__201108222256.wav')
time = np.arange(0, len(data)) / sfreq

audio = pd.Series(data, index=time)[:1.0]
audio.index.name = 'time'

'''
INSTRUCTIONS 1/3

*   Visualize the raw audio you'll use to calculate the envelope.
'''

# Plot the raw data first
audio.plot(figsize=(10, 5))
plt.show()

'''
INSTRUCTIONS 2/3

*   Rectify the audio.
*   Plot the result.
'''

# Rectify the audio signal
audio_rectified = audio.apply(np.abs)

# Plot the result
audio_rectified.plot(figsize=(10, 5))
plt.show()

'''
INSTRUCTIONS 3/3

*   Smooth the audio file by applying a rolling mean.
*   Plot the result.
'''

# Smooth by applying a rolling mean
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# Plot the result
audio_rectified_smooth.plot(figsize=(10, 5))
plt.show()