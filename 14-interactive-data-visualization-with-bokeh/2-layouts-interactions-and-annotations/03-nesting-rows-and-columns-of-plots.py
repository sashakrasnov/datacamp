'''
Nesting rows and columns of plots

You can create nested layouts of plots by combining row and column layouts.

In this exercise, you'll make a 3-plot layout in two rows using the auto-mpg data set.

Three plots have been created for you of average mpg vs year, mpg vs hp, and mpg vs weight.

Your job is to use the column() and row() functions to make a two-row layout where the first row will have only the average mpg vs year plot and the second row will have mpg vs hp and mpg vs weight plots as columns.

By using the sizing_mode argument, you can scale the widths to fill the whole figure.
'''

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv('../datasets/auto-mpg.csv')

mpg_mean = df.groupby('yr')['mpg'].mean()

mpg_hp = figure(x_axis_label='weight', y_axis_label='mpg')
mpg_hp.circle(df.weight.values, df.mpg.values)

mpg_weight = figure(x_axis_label='hp', y_axis_label='mpg')
mpg_weight.circle(df.hp.values, df.mpg.values)

avg_mpg = figure(x_axis_label='year', y_axis_label='mean mpg')
avg_mpg.line(mpg_mean.index.values, mpg_mean.values)

'''
INSTRUCTIONS

*   Import row and column from bokeh.layouts.
*   Create a column layout called row2 with the figures mpg_hp and mpg_weight in a list and set *   sizing_mode='scale_width'.
*   Create a row layout called layout with the figure avg_mpg and the column layout row2 in a list and set sizing_mode='scale_width'.
'''

# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a column layout that will be used as the second row: row2
row2 = column([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a row layout that includes the above column layout: layout
layout = row([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)
