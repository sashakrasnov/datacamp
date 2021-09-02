'''
Learn about widget callbacks

You'll now learn how to use widget callbacks to update the state of a Bokeh application, and in turn, the data that is presented to the user.

Your job in this exercise is to use the slider's on_change() function to update the plot's data from the previous example. NumPy's sin() function will be used to update the y-axis data of the plot.

Now that you have added a widget callback, notice how as you move the slider of your app, the figure also updates!
'''

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import widgetbox, column, row
from bokeh.models import Slider
from bokeh.plotting import ColumnDataSource, figure

def_scale = 1

x = np.linspace(0.3, 10, 300)
y = np.sin(def_scale/x)

source = ColumnDataSource(data={'x': x, 'y': y})

slider = Slider(title='scale', start=1, end=10, step=0.1, value=def_scale)

plot = figure(x_axis_label='X', y_axis_label='y = sin(scale/X)')
plot.line('x', 'y', source=source)

'''
INSTRUCTIONS

*   Define a callback function callback with the parameters attr, old, new.
*   Read the current value of slider as a variable scale. You can do this using slider.value.
*   Compute values for the updated y using np.sin(scale/x).
*   Update source.data with the new data dictionary.
*   Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and callback
'''

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)
