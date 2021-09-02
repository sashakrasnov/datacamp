'''
Sampling with replacement

In this example, you will review the np.random.choice() function that you've already seen in the previous chapters. You are given multiple variations of np.random.choice() for sampling from arrays. Look at each variation carefully and select the one that could generate the output. ['a', 'c', 'c'] as an output.
'''

import numpy as np

'''
INSTRUCTIONS

Possible Answers:

o   np.random.choice(['a', 'b', 'c'], size=3, replace=False)
*   np.random.choice(['a', 'b', 'c', 'd', 'e'], size=5, replace=True)[:3]
o   np.random.choice(['a', 'b', 'c', 'd', 'e'], size=5, replace=False)[:3]
o   np.random.choice(['a', 'b'], size=3, replace=True)
'''

print(np.random.choice(['a', 'b', 'c', 'd', 'e'], size=5, replace=True)[:3])