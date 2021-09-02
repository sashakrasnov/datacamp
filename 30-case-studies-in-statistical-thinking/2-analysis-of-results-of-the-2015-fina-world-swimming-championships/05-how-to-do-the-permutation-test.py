'''
How to do the permutation test
Based on our EDA and parameter estimates, it is tough to discern improvement from the semifinals to finals. In the next exercise, you will test the hypothesis that there is no difference in performance between the semifinals and finals. A permutation test is fitting for this. We will use the mean value of f as the test statistic. Which of the following simulates getting the test statistic under the null hypothesis?

Strategy 1
*   Take an array of semifinal times and an array of final times for each swimmer for each stroke/distance pair.
*   Go through each array, and for each index, swap the entry in the respective final and semifinal array with a 50% probability.
*   Use the resulting final and semifinal arrays to compute f and then the mean of f.

Strategy 2
*   Take an array of semifinal times and an array of final times for each swimmer for each stroke/distance pair and concatenate them, giving a total of 96 entries.
*   Scramble the concatenated array using the np.permutation() function. Assign the first 48 entries in the scrambled array to be "semifinal" and the last 48 entries to be "final."
*   Compute f from these new semifinal and final arrays, and then compute the mean of f.

Strategy 3
*   Take the array f we used in the last exercise.
*   Multiply each entry of f by either 1 or -1 with equal probability.
*   Compute the mean of this new array to get the test statistic.

Strategy 4
*   Define a function with signature compute_f(semi_times, final_times) to compute f from inputted swim time arrays.
*   Draw a permutation replicate using dcst.draw_perm_reps(semi_times, final_times, compute_f).

INSTRUCTIONS

Possible Answers

*   Strategy 1
o   Strategy 2
o   Strategy 3
o   Strategy 4
'''
