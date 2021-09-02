'''
Computing the value of a formal ECDF

To be able to do the Kolmogorov-Smirnov test, we need to compute the value of a formal ECDF at arbitrary points. In other words, we need a function, ecdf_formal(x, data) that returns the value of the formal ECDF derived from the data set data for each value in the array x. Two of the functions accomplish this. One will not. Of the two that do the calculation correctly, one is faster. Label each.

As a reminder, the ECDF is formally defined as ECDF(x) = (number of samples ≤ x) / (total number of samples). You also might want to check out the doc string of np.searchsorted().

a)
|   def ecdf_formal(x, data):
|       return np.searchsorted(np.sort(data), x) / len(data)

b)
|   def ecdf_formal(x, data):
|       return np.searchsorted(np.sort(data), x, side='right') / len(data)

c)
|   def ecdf_formal(x, data):
|       output = np.empty(len(x))
|
|       data = np.sort(data)
|
|       for i, x_val in x:
|           j = 0
|           while j < len(data) and x_val >= data[j]:
|               j += 1
|
|           output[i] = j
|
|       return output / len(data)

INSTRUCTIONS

Possible Answers:

o   (a) Correct, fast; (b) Incorrect; (c) Correct, slow.
o   (a) Correct, slow; (b) Incorrect; (c) Correct, fast.
*   (a) Incorrect; (b) Correct, fast; (c) Correct, slow. // Correct! (a) will fail if a value in x is directly on one of the data points.
o   (a) Incorrect; (b) Correct, slow; (c) Correct, fast.
'''