'''
Enhancing the plot with some shading

Now that you have the base plot ready, you can enhance it by coloring each circle glyph by continent.

Your job is to make a list of the unique regions from the data frame, prepare a ColorMapper, and add it to the circle glyph.
'''

import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

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

'''
INSTRUCTIONS

*   Make a list of the unique values from the region column. You can use the unique() and tolist() methods on data.region to do this.
*   Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes.
*   Use the CategoricalColorMapper() function to make a color mapper called color_mapper with factors=regions_list and palette=Spectral6.
*   Add the color mapper to the circle glyph as a dictionary with dict(field='region', transform=color_mapper) as the argument passed to the color parameter of plot.circle(). Also set the legend parameter to be the 'region'.
*   Set the legend.location attribute of plot to 'top_right'.
'''

# Make a list of the unique values from the region column: regions_list
regions_list = data.region.unique().tolist()

# Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'

# Add the plot to the current document and add the title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'