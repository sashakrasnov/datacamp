'''
How to combine Bokeh models into layouts

Let's begin making a Bokeh application that has a simple slider and plot, that also updates the plot based on the slider.

In this exercise, your job is to first explicitly create a ColumnDataSource. You'll then combine a plot and a slider into a single column layout, and add it to the current document.

After you are done, notice how in the figure you generate, the slider will not actually update the plot, because a widget callback has not been defined. You'll learn how to update the plot using widget callbacks in the next exercise.

All the necessary modules have been imported for you. The plot is available in the workspace as plot, and the slider is available as slider.
'''

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import widgetbox, column, row
from bokeh.models import Slider
from bokeh.plotting import ColumnDataSource, figure

x = np.linspace(0.3, 10, 300)
y = x * np.sin(x) - x

slider = Slider(title='slider', start=10, end=100, step=0.1, value=2)

plot = figure(x_axis_label='X', y_axis_label='y = X * sin(X) - X')

'''
INSTRUCTIONS

*   Create a ColumnDataSource called source. Explicitly specify the data parameter of ColumnDataSource() with {'x': x, 'y': y}.
*   Add a line to the figure plot, with 'x' and 'y' from the ColumnDataSource.
*   Combine the slider and the plot into a column layout called layout. Be sure to first create a widgetbox layout using widgetbox() with slider and pass that into the column() function along with plot.
'''

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)