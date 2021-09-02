'''
Power Analysis - Part I

Now we turn to power analysis. You typically want to ensure that any experiment or A/B test you run has at least 80% power. One way to ensure this is to calculate the sample size required to achieve 80% power.

Suppose that you are in charge of a news media website and you are interested in increasing the amount of time users spend on your website. Currently, the time users spend on your website is normally distributed with a mean of 1 minute and a variance of 0.5 minutes. Suppose that you are introducing a feature that loads pages faster and want to know the sample size required to measure a 10% increase in time spent on the website.

In this exercise, we will set up the framework to run one simulation, run a t-test & calculate the p-value.
'''

import numpy as np
import scipy.stats.stats as st

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

'''
INSTRUCTIONS

*   Initialize effect_size to 5%, control_mean to 1 and control_sd to 0.5.
*   Using np.random.normal() simulate one drawing of control_time_spent and treatment_time_spent.
*   Run a t-test on treatment_time_spent and control_time_spent using st.ttest_ind() where st is scipy.stats, which is already imported.
*   Statistical significance should be True if p_value is less than 0.05, otherwise it should be False.
'''

# Initialize effect_size, control_mean, control_sd
effect_size, sample_size, control_mean, control_sd = 0.05, 50, 1, 0.5

# Simulate control_time_spent and treatment_time_spent, assuming equal variance
control_time_spent = np.random.normal(loc=control_mean, scale=control_sd, size=sample_size)
treatment_time_spent = np.random.normal(loc=control_mean*(1+effect_size), scale=control_sd, size=sample_size)

# Run the t-test and get the p_value
t_stat, p_value = st.ttest_ind(treatment_time_spent, control_time_spent)
print("P-value: {}, Statistically Significant? {}".format(p_value, p_value < effect_size))