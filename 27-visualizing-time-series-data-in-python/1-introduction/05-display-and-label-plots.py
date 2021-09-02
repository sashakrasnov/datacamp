'''
Display and label plots

As you saw earlier, if the index of a pandas DataFrame consists of dates, then pandas will automatically format the x-axis in a human-readable way. In addition the .plot() method allows you to specify various other parameters to tailor your time series plot (color of the lines, width of the lines and figure size).

You may have noticed the use of the notation ax = df.plot(...) and wondered about the purpose of the ax object. This is because the plot function returns a matplotlib AxesSubplot object, and it is common practise to assign this returned object to a variable called ax. Doing so also allows you to include additional notations and specifications to your plot such as axis labels.
'''

import pandas as pd
import matplotlib.pyplot as plt

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)
discoveries = discoveries.set_index('date')

'''
INSTRUCTIONS

Display a line chart of the discoveries DataFrame.

*   Specify the color of the line as 'blue'.
*   Width of the line as 2.
*   The dimensions of your plot to be of length 8 and width 3.
*   Specify the fontsize of 6.
'''

# Plot a line chart of the discoveries DataFrame using the specified arguments
ax = discoveries.plot(color='blue', figsize=(8, 3), linewidth=2, fontsize=6)

# Specify the title in your plot
ax.set_title('Number of great inventions and scientific discoveries from 1860 to 1959', fontsize=8)

# Show plot
plt.show()