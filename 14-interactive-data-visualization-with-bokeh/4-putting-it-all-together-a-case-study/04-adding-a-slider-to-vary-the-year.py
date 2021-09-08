'''
Adding a slider to vary the year

Until now, we've been plotting data only for 1970. In this exercise, you'll add a slider to your plot to change the year being plotted. To do this, you'll create an update_plot() function and associate it with a slider to select values between 1970 and 2010.

After you are done, you may have to scroll to the right to view the entire plot. As you play around with the slider, notice that the title of the plot is not updated along with the year. This is something you'll fix in the next exercise!
'''

import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6

data = pd.read_csv('../datasets/gapminder_tidy.csv', index_col='Year')

source = ColumnDataSource(data={
    'x'      : data.loc[1970].fertility,
    'y'      : data.loc[1970].life,
    'country': data.loc[1970].Country,
    'pop'    : data.loc[1970].population / 20000000 + 2,
    'region' : data.loc[1970].region,
})

xmin, xmax = min(data.fertility), max(data.fertility)
ymin, ymax = min(data.life), max(data.life)

plot = figure(
    title='Gapminder Data for 1970',
    plot_height=400, plot_width=700,
    x_range=(xmin, xmax), y_range=(ymin, ymax))

regions_list = data.region.unique().tolist()

color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

plot.circle(
    x='x', y='y', fill_alpha=0.8, source=source,
    color=dict(field='region', transform=color_mapper), legend='region')

plot.legend.location = 'top_right'

curdoc().title = 'Gapminder'

'''
INSTRUCTIONS

*   Import the widgetbox and row functions from bokeh.layouts, and the Slider function from bokeh.models.
*   Define the update_plot callback function with parameters attr, old and new.
*   Set the yr name to slider.value and set source.data = new_data.
*   Make a slider object called slider using the Slider() function with a start year of 1970, end year of 2010, step of 1, value of 1970, and title of 'Year'.
*   Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and update_plot.
*   Make a row layout of widgetbox(slider) and plot and add it to the current document.
'''

# Import the necessary modules
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # set the `yr` name to `slider.value` and `source.data = new_data`
    yr = slider.value
    new_data = {
        'x'      : data.loc[yr].fertility,
        'y'      : data.loc[yr].life,
        'country': data.loc[yr].Country,
        'pop'    : data.loc[yr].population / 20000000 + 2,
        'region' : data.loc[yr].region,
    }
    source.data = new_data


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)

# To start bokeh server run this command in the current folder
# bokeh serve --show 04-adding-a-slider-to-vary-the-year.py