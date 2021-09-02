'''
A scatter plot with different shapes

By calling multiple glyph functions on the same figure object, we can overlay multiple data sets in the same figure.

In this exercise, you will plot female literacy vs fertility for two different regions, Africa and Latin America. Each set of x and y data has been loaded separately for you as fertility_africa, female_literacy_africa, fertility_latinamerica, and female_literacy_latinamerica.

Your job is to plot the Latin America data with the circle() glyph, and the Africa data with the x() glyph.

figure has already been imported for you from bokeh.plotting.
'''

from bokeh.plotting import figure
from bokeh.io import output_file, show

fertility_latinamerica = [
    1.827, 2.156, 2.404, 2.223, 2.53, 2.498, 1.926, 4.018, 2.513, 1.505, 2.612, 3.371,
    3.19, 2.977, 2.295, 2.683, 1.943, 2.516, 2.089, 2.362, 1.647, 2.373, 3.371, 1.732
]
female_literacy_latinamerica = [
    90.2, 91.5, 93.4, 97.7, 84.6, 94.9, 98.7, 68.7, 81.7, 99.8, 88.3, 86.0,
    83.5, 93.5, 81.4, 77.9, 96.2, 92.8, 98.5, 90.8, 98.2, 88.4, 96.5, 98.0
]

fertility_africa = [
    5.173, 2.816, 5.211, 5.908, 2.505, 5.520, 4.058, 4.859, 2.342, 6.254, 2.334, 4.220,
    4.967, 4.514, 4.620, 4.541, 5.637, 5.841, 5.455, 7.069, 5.405, 5.737, 3.363, 4.890,
    6.081, 1.841, 5.329, 5.330, 5.378, 4.450, 4.166, 2.642, 5.165, 4.528, 4.697, 5.011,
    4.388, 3.290, 3.264, 2.822, 4.969, 5.659, 3.240, 1.792, 3.450, 5.283, 3.885, 2.663,
    3.718
]
female_literacy_africa = [
    48.8, 57.8, 22.8, 56.1, 88.1, 66.3, 59.6, 82.8, 63.9, 66.8, 44.1, 59.3, 40.1, 44.3,
    65.3, 67.8, 57.0, 21.6, 65.8, 15.1, 18.2, 61.0, 88.8, 33.0, 21.9, 71.0, 26.4, 66.1,
    28.1, 59.9, 53.7, 81.3, 28.9, 54.5, 41.1, 53.0, 49.5, 87.7, 95.1, 83.5, 34.3, 36.5,
    83.2, 84.8, 85.6, 89.1, 67.8, 79.3, 83.3
]

'''
INSTRUCTIONS

*   Create the figure p with the figure() function. It has two parameters: x_axis_label and y_axis_label.
*   Add a circle glyph to the figure p using the function p.circle() where the inputs are the x and y data from Latin America: fertility_latinamerica and female_literacy_latinamerica.
*   Add an x glyph to the figure p using the function p.x() where the inputs are the x and y data from Africa: fertility_africa and female_literacy_africa.
*   The code to create, display, and specify the name of the output file has been written for you, so after adding the x glyph, hit 'Submit Answer' to view the figure.
'''

# Create the figure: p
p = figure(x_axis_label='fertility', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)
