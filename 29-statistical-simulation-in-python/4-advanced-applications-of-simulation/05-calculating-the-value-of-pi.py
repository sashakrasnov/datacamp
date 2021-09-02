'''
Calculating the value of pi

Now we work through a classic example - estimating the value of π.

Imagine a square of side 2 with the origin (0,0) as its center and the four corners having coordinates (1,1), (1,−1), (−1,1), (−1,−1). The area of this square is 2×2=4. Now imagine a circle of radius 1 with its center at the origin fitting perfectly inside this square. The area of the circle will be π × radius^2 = π.

To estimate π, we randomly sample multiple points in this square & get the fraction of points inside the circle (x^2 + y^2 <= 1). The area of the circle then is 4 times this fraction, which gives us our estimate of π.

After this exercise, you'll have a grasp of how to use simulation for computation.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Examine the true value of pi using np.pi in the console. Initialize sims to 10000 and circle_points to 0.
*   Within the for loop, generate a point (x & y coordinates) using np.random.uniform() between -1 and 1, having size=2.
*   Check if the point lies within the unit circle with the equation x2+y2<=1, assign to within_circle, and increment circle_points accordingly.
*   Print the estimate of pi, which is 4 times the fraction of points that lie within the circle.
'''

# Initialize sims and circle_points
sims, circle_points = 10000 , 0 

for i in range(sims):
    # Generate the two coordinates of a point
    point = np.random.uniform(-1, 1, size=2)
    # if the point lies within the unit circle, increment counter
    within_circle = point[0]**2 + point[1]**2 <= 1
    if within_circle == True:
        circle_points += 1
        
# Estimate pi as 4 times the avg number of points in the circle.
print("Simulated value of pi = {}".format(4*circle_points/sims))