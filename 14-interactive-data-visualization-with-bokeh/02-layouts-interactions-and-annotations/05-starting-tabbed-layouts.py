'''
Starting tabbed layouts

Tabbed layouts can be created in Pandas by placing plots or layouts in Panels.

In this exercise, you'll take the four fertility vs female literacy plots from the last exercise and make a Panel() for each.

No figure will be generated in this exercise. Instead, you will use these panels in the next exercise to build and display a tabbed layout.
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

*   Import Panel from bokeh.models.widgets.
*   Create a new panel tab1 with child p1 and a title of 'America'.
*   Create a new panel tab2 with child p2 and a title of 'Asia'.
*   Create a new panel tab3 with child p3 and a title of 'Africa'.
*   Create a new panel tab4 with child p4 and a title of 'Europe'.
*   Click submit to check your work.
'''

# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Asia')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Africa')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')
