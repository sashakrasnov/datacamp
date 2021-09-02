'''
Customizing your scatter plots

The three most important arguments to customize scatter glyphs are color, size, and alpha. Bokeh accepts colors as hexadecimal strings, tuples of RGB values between 0 and 255, and any of the 147 CSS color names. Size values are supplied in screen space units with 100 meaning the size of the entire figure.

The alpha parameter controls transparency. It takes in floating point numbers between 0.0, meaning completely transparent, and 1.0, meaning completely opaque.

In this exercise, you'll plot female literacy vs fertility for Africa and Latin America as red and blue circle glyphs, respectively.
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

*   Using the Latin America data (fertility_latinamerica and female_literacy_latinamerica), add a blue circle glyph of size=10 and alpha=0.8 to the figure p. To do this, you will need to specify the color, size and alpha keyword arguments inside p.circle().
*   Using the Africa data (fertility_africa and female_literacy_africa), add a red circle glyph of size=10 and alpha=0.8 to the figure p.
'''

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue', size=10, alpha=0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color='red', size=10, alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)
