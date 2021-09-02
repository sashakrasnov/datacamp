'''
How to create legends

Legends can be added to any glyph by using the legend keyword argument.

In this exercise, you will plot two circle glyphs for female literacy vs fertility in Africa and Latin America.

Two ColumnDataSources called latin_america and africa have been provided.

Your job is to plot two circle glyphs for these two objects with fertility on the x axis and female_literacy on the y axis and add the legend values. The figure p has been provided for you.
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
africa = ColumnDataSource(africa_d)

p = figure(x_axis_label='fertility (children per woman)', y_axis_label='life')

'''
INSTRUCTIONS

*   Add a red circle glyph to the figure p using the latin_america ColumnDataSource. Specify a size of 10 and legend of America.
*   Add a blue circle glyph to the figure p using the africa ColumnDataSource. Specify a size of 10 and legend of Africa.
'''

# Add the first circle glyph to the figure p
p.circle('fertility', 'life', source=america, size=10, color='red', legend='America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'life', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
output_file('fert_life_groups.html')
show(p)
