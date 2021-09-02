'''
Displaying tabbed layouts

Tabbed layouts are collections of Panel objects. Using the figures and Panels from the previous two exercises, you'll create a tabbed layout to change the region in the fertility vs female literacy plots.

Your job is to create the layout using Tabs() and assign the tabs keyword argument to your list of Panels. The Panels have been created for you as tab1, tab2, tab3 and tab4.

After you've displayed the figure, explore the tabs you just added! The "Pan", "Box Zoom" and "Wheel Zoom" tools are also all available as before.
'''

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models.widgets import Panel

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

tab1 = Panel(child=p1, title='America')
tab2 = Panel(child=p2, title='Asia')
tab3 = Panel(child=p3, title='Africa')
tab4 = Panel(child=p4, title='Europe')

'''
INSTRUCTIONS

*   Import Tabs from bokeh.models.widgets.
*   Create a Tabs layout called layout with tab1, tab2, tab3, and tab4.
Click 'Submit Answer' to output the file and show the figure.
'''

# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)
