'''
Lines and markers

Lines and markers can be combined by plotting them separately using the same data points.

In this exercise, you'll plot a line and circle glyph for the AAPL stock prices. Further, you'll adjust the fill_color keyword argument of the circle() glyph function while leaving the line_color at the default value.

The date and price lists are provided. The Bokeh figure object p that you created in the previous exercise has also been provided.
'''

import pandas as pd
from bokeh.io import output_file, show

aapl = pd.read_csv('../datasets/aapl.csv')

date = list(pd.DatetimeIndex(aapl['date']).to_pydatetime())[:102]
price = list(aapl['adj_close'].values)[:102]

'''
INSTRUCTIONS

*   Plot date along the x-axis and price along the y-axis with p.line().
*   With date on the x-axis and price on the y-axis, use p.circle() to add a 'white' circle glyph of size 4. To do this, you will need to specify the fill_color and size arguments.
'''

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x-axis and price along the y-axis
p.line(date, price)

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)
