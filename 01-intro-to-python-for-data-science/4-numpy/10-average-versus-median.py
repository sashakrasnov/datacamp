'''
Average versus median

You now know how to use numpy functions to get a better feeling for your data.
It basically comes down to importing numpy and then calling several simple functions on the numpy arrays:

|   import numpy as np
|   x = [1, 4, 8, 10, 12]
|   np.mean(x)
|   np.median(x)

The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.
'''

from random import uniform
import numpy as np

height_in = [uniform(71, 85) for _ in range(1015)]
weight_lb = [h * uniform(2.2, 2.5) for h in height_in]
age = [uniform(20, 35) for _ in range(1015)]

baseball = list(zip(weight_lb, height_in, age))
np_baseball = np.array(baseball)

'''
Instructions

*   Create numpy array np_height that is equal to first column of np_baseball.
*   Print out the mean of np_height.
*   Print out the median of np_height.
'''

# np_baseball is available


# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np.array(np_baseball[:, 0])

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
