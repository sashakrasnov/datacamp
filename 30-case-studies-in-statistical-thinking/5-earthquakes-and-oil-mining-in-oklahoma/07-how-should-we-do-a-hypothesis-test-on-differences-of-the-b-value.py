'''
How should we do a hypothesis test on differences of the b-value?

We wish to test the hypothesis that the b-value in Oklahoma from 1980 through 2009 is the same as that from 2010 through mid-2017. Which of the first five statements is false? If none of them are false, select the last choice.
'''

import numpy as np
import pandas as pd
import dc_stat_think as dcst

def b_value(mags, mt, perc=[2.5, 97.5], n_reps=None):
    """Compute the b-value and optionally its confidence interval."""
    # Extract magnitudes above completeness threshold: m
    m = mags[mags >= mt]

    # Compute b-value: b
    b = (np.mean(m) - mt) * np.log(10)

    # Draw bootstrap replicates
    if n_reps is None:
        return b
    else:
        m_bs_reps = dcst.draw_bs_reps(m, np.mean, size=n_reps)

        # Compute b-value from replicates: b_bs_reps
        b_bs_reps = (m_bs_reps - mt) * np.log(10)

        # Compute confidence interval: conf_int
        conf_int = np.percentile(b_bs_reps, perc)
    
        return b, conf_int


df = pd.read_csv('../datasets/oklahoma_earthquakes_1950-2017.csv', comment='#', index_col='time', parse_dates=True, usecols=['time','mag'])

time = np.array([d.timestamp() / 31556925.9747 + 1970 for d in df['1980-01':'2017-06'].index.to_pydatetime()])
mags = df['1980-01':'2017-06'].mag.values

mt = 3

# Get magnitudes before and after 2010
mags_pre = mags[time < 2010]
mags_post = mags[time >= 2010]

'''
INSTRUCTIONS

Possible Answers:

o   You should only include earthquakes that have magnitudes above the completeness threshold. A value of 3 is reasonable. // This is true because below the completeness threshold, we are not comparing earthquakes before and after 2010, but observed earthquakes before and after 2010. We do not have a complete data set below the completeness threshold.
o   You should perform a permutation test because asserting a null hypothesis that the b-values are the same implicitly assumes that the magnitudes are identically distributed, specifically Exponentially, by the Gutenberg-Richter Law. // This is true. We really are assuming the Gutenberg-Richter law holds, in part because we are only considering earthquakes above the completeness threshold. We are using a model (the G-R law) to deal with missing data. So, since both sets of quakes follow the same statistical model, and that model has a single parameter, a permutation test is appropriate.
o   A reasonable test statistic is the difference between the mean post-2010 magnitude and the mean pre-2010 magnitude. // This is true. You may be thinking that the mean values are not the b-values, and that you should be using the difference in b-value as your test statistic. However, the difference in mean magnitude is directly proportional to the difference in b-value, so the result of the hypothesis test will be identical if we use b-values of mean magnitudes.
o    You do not need to worry about the fact that there were far fewer earthquakes before 2010 than there were after. That is to say, there are fewer earthquakes before 2010, but sufficiently many to do a permutation test. // This is true. Even though they have different numbers of earthquakes, you are only interested in summary statistics about their magnitude. There were 53 earthquakes between 1980 and 2009 with magnitude 3 or greater, so we have enough to compute a reliable mean.
o   You do not need to worry about the fact that the two time intervals are of different length.
None of the above statements are false. // Provided the time interval is long enough, the b-value is independent of the time interval, just like the mean of Exponentially distributed values is independent of how many there are, provided there are not too few.
*   None of the above statements are false. // Correct! For instructional purposes, here are reasons why each is true: Option 1 is true because below the completeness threshold, we are not comparing earthquakes before and after 2010, but observed earthquakes before and after 2010. We do not have a complete data set below the completeness threshold. Option 2 is true because we really are assuming the Gutenberg-Richter law holds, in part because we are only considering earthquakes above the completeness threshold. We are using a model (the G-R law) to deal with missing data. So, since both sets of quakes follow the same statistical model, and that model has a single parameter, a permutation test is appropriate. Option 3 is true, even though you may be thinking that the mean values are not the b-values, and that you should be using the difference in b-value as your test statistic. However, the difference in mean magnitude is directly proportional to the difference in b-value, so the result of the hypothesis test will be identical if we use b-values of mean magnitudes. Option 4 is true because even though they have different numbers of earthquakes, you are only interested in summary statistics about their magnitude. There were 53 earthquakes between 1980 and 2009 with magnitude 3 or greater, so we have enough to compute a reliable mean. Option 5 is true because, provided the time interval is long enough, the b-value is independent of the time interval, just like the mean of Exponentially distributed values is independent of how many there are, provided there are not too few.
'''