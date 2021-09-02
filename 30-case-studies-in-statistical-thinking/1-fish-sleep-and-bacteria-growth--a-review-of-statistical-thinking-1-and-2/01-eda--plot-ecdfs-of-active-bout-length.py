'''
EDA: Plot ECDFs of active bout length

An active bout is a stretch of time where a fish is constantly moving. Plot an ECDF of active bout length for the mutant and wild type fish for the seventh night of their lives. The data sets are in the numpy arrays bout_lengths_wt and bout_lengths_mut. The bout lengths are in units of minutes.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datasets/gandhi_et_al_bouts.csv', comment='#')

bout_lengths_wt  = df[df.genotype=='wt'].bout_length.values
bout_lengths_mut = df[df.genotype=='mut'].bout_length.values

'''
INSTRUCTIONS

*   Import the module dc_stat_think as dcst so you have its functions available.
*   Generate the x and y values for plotting the ECDF of the wild type fish (bout_lengths_wt) using dcst.ecdf(). Store the result in numpy arrays named x_wt and y_wt.
*   Do the same for the the mutant fish (bout_lengths_mut), storing the result in numpy arrays named x_mut and y_mut.
*   Use plt.plot() to plot the two ECDFs as dots on the same plot. Be sure to specify the keyword arguments marker='.' and linestyle='none'.
*   Show your plot using plt.show().
'''

# Import the dc_stat_think module as dcst
import dc_stat_think as dcst

# Generate x and y values for plotting ECDFs
x_wt, y_wt = dcst.ecdf(bout_lengths_wt)
x_mut, y_mut = dcst.ecdf(bout_lengths_mut)

# Plot the ECDFs
_ = plt.plot(x_wt, y_wt, marker='.', linestyle='none')
_ = plt.plot(x_mut, y_mut, marker='.', linestyle='none')

# Make a legend, label axes, and show plot
_ = plt.legend(('wt', 'mut'))
_ = plt.xlabel('active bout length (min)')
_ = plt.ylabel('ECDF')
plt.show()
