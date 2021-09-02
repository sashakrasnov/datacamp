'''
Using subplot() (2)

Now you have some familiarity with plt.subplot(), you can use it to plot more plots in larger grids of subplots of the same figure.

Here, you will make a 2×2 grid of subplots and plot the percentage of degrees awarded to women in Physical Sciences (using physical_sciences), in Computer Science (using computer_science), in Health Professions (using health), and in Education (using education).
'''

import numpy as np
import matplotlib.pyplot as plt

physical_sciences = np.array([
    13.8, 14.9, 14.8, 16.5, 18.2, 19.1, 20. , 21.3, 22.5, 23.7, 24.6, 25.7, 27.3, 27.6,
    28. , 27.5, 28.4, 30.4, 29.7, 31.3, 31.6, 32.6, 32.6, 33.6, 34.8, 35.9, 37.3, 38.3,
    39.7, 40.2, 41. , 42.2, 41.1, 41.7, 42.1, 41.6, 40.8, 40.7, 40.7, 40.7, 40.2, 40.1])

computer_science = np.array([
    13.6, 13.6, 14.9, 16.4, 18.9, 19.8, 23.9, 25.7, 28.1, 30.2, 32.5, 34.8, 36.3, 37.1,
    36.8, 35.7, 34.7, 32.4, 30.8, 29.9, 29.4, 28.7, 28.2, 28.5, 28.5, 27.5, 27.1, 26.8,
    27. , 28.1, 27.7, 27.6, 27. , 25.1, 22.2, 20.6, 18.6, 17.6, 17.8, 18.1, 17.6, 18.2])

health = np.array([
    77.1, 75.5, 76.9, 77.4, 77.9, 78.9, 79.2, 80.5, 81.9, 82.3, 83.5, 84.1, 84.4, 84.6,
    85.1, 85.3, 85.7, 85.5, 85.2, 84.6, 83.9, 83.5, 83. , 82.4, 81.8, 81.5, 81.3, 81.9,
    82.1, 83.5, 83.5, 85.1, 85.8, 86.5, 86.5, 86. , 85.9, 85.4, 85.2, 85.1, 85. , 84.8])

education = np.array([
    74.53532758, 74.14920369, 73.55451996, 73.50181443, 73.33681143, 72.80185448, 72.16652471,
    72.45639481, 73.19282134, 73.82114234, 74.98103152, 75.84512345, 75.84364914, 75.95060123,
    75.86911601, 75.92343971, 76.14301516, 76.96309168, 77.62766177, 78.11191872, 78.86685859,
    78.99124597, 78.43518191, 77.26731199, 75.81493264, 75.12525621, 75.03519921, 75.1637013 ,
    75.48616027, 75.83816206, 76.69214284, 77.37522931, 78.64424394, 78.54494815, 78.65074774,
    79.06712173, 78.68630551, 78.72141311, 79.19632674, 79.5329087 , 79.61862451, 79.43281184])

year = np.array([y for y in range(1970,2012)])

'''
INSTRUCTIONS

*   Create a figure with 2×2 subplot layout, make the top, left subplot active, and plot the % of degrees awarded to women in Physical Sciences in blue in the active subplot.
*   Make the top, right subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Computer Science in red in the active subplot.
*   Make the bottom, left subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Health Professions in green in the active subplot.
*   Make the bottom, right subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Education in yellow in the active subplot.
'''

# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
