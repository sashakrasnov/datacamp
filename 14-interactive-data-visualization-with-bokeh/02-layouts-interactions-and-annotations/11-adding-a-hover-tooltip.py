'''
Adding a hover tooltip

Working with the HoverTool is easy for data stored in a ColumnDataSource.

In this exercise, you will create a HoverTool object and display the country for each circle glyph in the figure that you created in the last exercise. This is done by assigning the tooltips keyword argument to a list-of-tuples specifying the label and the column of values from the ColumnDataSource using the @ operator.

The figure object has been prepared for you as p.

After you have added the hover tooltip to the figure, be sure to interact with it by hovering your mouse over each point to see which country it represents.
'''

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import ColumnDataSource

df = pd.read_csv('../datasets/gapminder_tidy.csv').dropna()

america_df = df[df.region.str.contains('America')].groupby('Country').mean()
africa_df = df[df.region.str.contains('Africa')].groupby('Country').mean()

america = ColumnDataSource(america_df)
africa = ColumnDataSource(africa_df)

p = figure(x_axis_label='fertility (children per woman)', y_axis_label='life')

p.circle('fertility', 'life', source=america, size=10, color='red', legend='America')
p.circle('fertility', 'life', source=africa, size=10, color='blue', legend='Africa')

p.legend.location='bottom_left'
p.legend.background_fill_color='lightgray'

'''
INSTRUCTIONS

*   Import the HoverTool class from bokeh.models.
*   Use the HoverTool() function to create a HoverTool object called hover and set the tooltips argument to be [('Country','@Country')].
*   Use p.add_tools() with your HoverTool object to add it to the figure.
'''

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Country','@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)
