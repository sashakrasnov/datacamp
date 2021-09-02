'''
Drawing K-S replicates

Now, you need a function to draw Kolmogorov-Smirnov replicates out of a target distribution, f. Construct a function with signature draw_ks_reps(n, f, args=(), size=10000, n_reps=10000) to do so. Here, n is the number of data points, and f is the function you will use to generate samples from the target CDF. For example, to test against an Exponential distribution, you would pass np.random.exponential as f. This function usually takes arguments, which must be passed as a tuple. So, if you wanted to take samples from an Exponential distribution with mean x_mean, you would use the args=(x_mean,) keyword. The keyword arguments size and n_reps respectively represent the number of samples to take from the target distribution and the number of replicates to draw.
'''

import numpy as np
import dc_stat_think as dcst

'''
INSTRUCTIONS

*   Write a function with signature draw_ks_reps(n, f, args=(), size=10000, n_reps=10000) that does the following.
    *   Generate size samples from the target distribution f. Remember, to pass the args into the sampling function, you should use the f(*args, size=size) construction. Store the result as x_f.
    *   Initialize the replicates array, reps, as an empty array with n_reps entries.
    *   Write a for loop to do the following n_reps times.
        *   Draw n samples from f. Again, use *args in your function call. Store the result in the variable x_samp.
        *   Compute the K-S statistic using dcst.ks_stat(), which is the function you wrote in the previous exercise, conveniently stored in the dcst module. Store the result in the reps array.
    *   Return the array reps.
'''

def draw_ks_reps(n, f, args=(), size=10000, n_reps=10000):
    # Generate samples from target distribution
    x_f = f(*args, size=size)
    
    # Initialize K-S replicates
    reps = np.empty(n_reps)
    
    # Draw replicates
    for i in range(n_reps):
        # Draw samples for comparison
        x_samp = f(*args, size=n)
        
        # Compute K-S statistic
        reps[i] = dcst.ks_stat(x_f, x_samp)

    return reps

'''
And now you have yet another valuable tool (which we have again conveniently put in dcst.draw_ks_reps())! This will allow you to draw K-S replicates for use in K-S tests for arbitrary continuous distributions. You'll put it to use in the next exercise.
'''