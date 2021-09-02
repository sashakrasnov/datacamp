'''
Define the color palette of your plots

When visualizing multiple time series, it can be difficult to differentiate between various colors in the default color scheme.

To remedy this, you can define each color manually, but this may be time-consuming. Fortunately, it is possible to leverage the colormap argument to .plot() to automatically assign specific color palettes with varying contrasts. You can either provide a matplotlib colormap as an input to this parameter, or provide one of the default strings that is available in the colormap() function available in matplotlib (all of which are available here -- http://matplotlib.org/examples/color/colormaps_reference.html).

For example, you can specify the 'viridis' colormap using the following command:

|   df.plot(colormap='viridis')
'''

import pandas as pd
import matplotlib.pyplot as plt

meat = pd.read_csv('../datasets/ch4_meat.csv', index_col=0, parse_dates=True)

'''
INSTRUCTIONS 1/2

*   Plot the time series data in the meat DataFrame and set the color palette to 'cubehelix'.
'''

# Plot time series dataset using the cubehelix color palette
ax = meat.plot(colormap='cubehelix', fontsize=15)

# Additional customizations
ax.set_xlabel('Date')
ax.legend(fontsize=18)

# Show plot
plt.show()

'''
INSTRUCTIONS 2/2

*   Plot the time series data in the meat DataFrame and set the color palette to 'PuOr'.
'''

# Plot time series dataset using the cubehelix color palette
ax = meat.plot(colormap='PuOr', fontsize=15)

# Additional customizations
ax.set_xlabel('Date')
ax.legend(fontsize=18)

# Show plot
plt.show()