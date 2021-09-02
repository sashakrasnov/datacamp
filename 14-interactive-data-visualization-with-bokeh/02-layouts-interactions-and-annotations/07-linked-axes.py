'''
Linked axes

Linking axes between plots is achieved by sharing range objects.

In this exercise, you'll link four plots of female literacy vs fertility so that when one plot is zoomed or dragged, one or more of the other plots will respond.

The four plots p1, p2, p3 and p4 along with the layout that you created in the last section have been provided for you.

Your job is link p1 with the three other plots by assignment of the .x_range and .y_range attributes.

After you have linked the axes, explore the plots by clicking and dragging along the x or y axes of any of the plots, and notice how the linked plots change together.
'''

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot

df = pd.read_csv('../datasets/gapminder_tidy.csv').dropna()

america = df[df.region.str.contains('America')].groupby('Country').mean()
asia = df[df.region.str.contains('Asia')].groupby('Country').mean()
africa = df[df.region.str.contains('Africa')].groupby('Country').mean()
europe = df[df.region.str.contains('Europe')].groupby('Country').mean()

p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='life', title='America')
p1.circle(america.fertility.values, america.life.values)

p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='life', title='Asia')
p2.circle(asia.fertility.values, asia.life.values)

p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='life', title='Africa')
p3.circle(africa.fertility.values, africa.life.values)

p4 = figure(x_axis_label='fertility (children per woman)', y_axis_label='life', title='Europe')
p4.circle(europe.fertility.values, europe.life.values)

row1 = [p1,p2]
row2 = [p3,p4]

layout = gridplot([row1,row2])

'''
INSTRUCTIONS

*   Link the x_range of p2 to p1.
*   Link the y_range of p2 to p1.
*   Link the x_range of p3 to p1.
*   Link the y_range of p4 to p1.
*   Click 'Submit Answer' to output the file and show the figure.
'''

# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p1.y_range

# Specify the name of the output_file and show the result
output_file('linked_range.html')
show(layout)
