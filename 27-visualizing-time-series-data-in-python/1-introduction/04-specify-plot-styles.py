'''
Specify plot styles

The matplotlib library also comes with a number of built-in stylesheets that allow you to customize the appearance of your plots. To use a particular style sheet for your plots, you can use the command plt.style.use(your_stylesheet) where your_stylesheet is the name of the style sheet.

In order to see the list of available style sheets that can be used, you can use the command print(plt.style.available). For the rest of this course, we will use the awesome fivethirtyeight style sheet.
'''

import pandas as pd

url_discoveries = '../datasets/ch1_discoveries.csv'

discoveries = pd.read_csv(url_discoveries)

discoveries['date'] = pd.to_datetime(discoveries.date)
discoveries = discoveries.set_index('date')

'''
INSTRUCTIONS 1/2

*   Import matplotlib.pyplot using its usual alias plt.
*   Use the fivethirtyeight style sheet to plot a line plot of the discoveries data.
'''

# Import the matplolib.pyplot sub-module
import matplotlib.pyplot as plt

# Use the fivethirtyeight style
plt.style.use('fivethirtyeight')

# Plot the time series
ax1 = discoveries.plot()
ax1.set_title('FiveThirtyEight Style')
plt.show()

'''
INSTRUCTIONS 2/2

*   Use the ggplot style sheet to plot a line plot of the discoveries data.
*   Set the title of your second plot as 'ggplot Style'.
'''

# Use the ggplot style
plt.style.use('ggplot')
ax2 = discoveries.plot()

# Set the title
ax2.set_title('ggplot Style')
plt.show()