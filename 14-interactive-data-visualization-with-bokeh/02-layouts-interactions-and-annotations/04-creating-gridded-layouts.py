'''
Creating gridded layouts

Regular grids of Bokeh plots can be generated with gridplot.

In this example, you're going to display four plots of fertility vs female literacy for four regions: Latin America, Africa, Asia and Europe.

Your job is to create a list-of-lists for the four Bokeh plots that have been provided to you as p1, p2, p3 and p4. The list-of-lists defines the row and column placement of each plot.
'''

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv('../datasets/gapminder_tidy.csv',).dropna()

america = df[df.region.str.contains('America')].groupby('Country').mean()
asia = df[df.region.str.contains('Asia')].groupby('Country').mean()
africa = df[df.region.str.contains('Africa')].groupby('Country').mean()
europe = df[df.region.str.contains('Europe')].groupby('Country').mean()

p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='mortality', title='America')
p1.circle(america.fertility.values, america.child_mortality.values)

p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='mortality', title='Asia')
p2.circle(asia.fertility.values, asia.child_mortality.values)

p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='mortality', title='Africa')
p3.circle(africa.fertility.values, africa.child_mortality.values)

p4 = figure(x_axis_label='fertility (children per woman)', y_axis_label='mortality', title='Europe')
p4.circle(europe.fertility.values, europe.child_mortality.values)

'''
INSTRUCTIONS

*   Import gridplot from the bokeh.layouts module.
*   Create a list called row1 containing plots p1 and p2.
*   Create a list called row2 containing plots p3 and p4.
*   Create a gridplot using row1 and row2. You will have to pass in row1 and row2 in the form of a list.
'''

# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1,p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3,p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1,row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)
