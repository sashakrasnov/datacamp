'''
Adding a hover tool

In this exercise, you'll practice adding a hover tool to drill down into data column values and display more detailed information about each scatter point.

After you're done, experiment with the hover tool and see how it displays the name of the country when your mouse hovers over a point!

The figure and slider have been created for you and are available in the workspace as plot and slider.
'''

import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider

data = pd.read_csv('../datasets/gapminder_tidy.csv', index_col='Year')

source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country'      : data.loc[1970].Country,
    'pop'      : (data.loc[1970].population / 20000000) + 2,
    'region'      : data.loc[1970].region,
})

xmin, xmax = min(data.fertility), max(data.fertility)
ymin, ymax = min(data.life), max(data.life)

plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700, x_range=(xmin, xmax), y_range=(ymin, ymax))

regions_list = data.region.unique().tolist()

color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

plot.legend.location = 'top_right'

curdoc().title = 'Gapminder'

def update_plot(attr, old, new):
    # Assign the value of the slider: yr
    yr = slider.value
    # Set new_data
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to: source.data
    source.data = new_data

    # Add title to figure: plot.title.text
    plot.title.text = 'Gapminder data for %d' % yr

slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

slider.on_change('value', update_plot)

'''
INSTRUCTIONS

*   Import HoverTool from bokeh.models.
*   Create a HoverTool object called hover with tooltips=[('Country', '@country')].
*   Add the HoverTool object you created to the plot using add_tools().
*   Create a row layout using widgetbox(slider) and plot.
*   Add the layout to the current document. This has already been done for you.
'''

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Create layout: layout
layout = row(widgetbox(slider), plot)

# Add layout to current document
curdoc().add_root(layout)
