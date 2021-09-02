'''
What can you conclude from this analysis?

All but one of the following constitute reasonable conclusions from our analysis of earthquakes. Which one does not?

    Parkfield 1950 through 2009
    b-value: 1.08
    95% conf int: [0.94, 1.23]


    Oklahoma 1980 through 2009
    b-value: 0.74
    95% conf int: [0.54, 0.97]

    mean time gap: 204.61 days
    95% conf int: [138.45, 276.83] days


    Oklahoma 2010 through mid-2017
    b-value: 0.62
    95% conf int: [0.60, 0.65]

    mean time gap: 1.12 days
    95% conf int: [0.97, 1.30] days

    Oklahoma: p-value for difference in b-value : 0.10

INSTRUCTIONS

Possible Answers

o   The seismicity, as measured by the b-value, is comparable before and after wastewater injection. // This is true. The confidence intervals of the b-values overlap, largely because we don't have so many earthquakes prior to 2010, and the p-value is about 0.1, suggesting we should not reject the null hypothesis that the b-value has not changed.
o   Earthquakes are over 100 times more frequent in Oklahoma after widespread wastewater injection began. // This is true. The time gap after 2010 is at least 100 times shorter after 2010, even taking the extremes of the confidence intervals for the time gap.
*   Oklahoma has a smaller b-value than the Parkfield region, so the Parkfield region has more earthquakes. // Correct! One cannot conclude information about frequency of earthquakes from the b-value alone. It is also true that from 2010-mid 2017, Oklahoma had twice as many earthquakes of magnitude 3 and higher than the entire state of California!
o   Oklahoma has a b-value smaller than the Parkfield region, so a randomly selected earthquake above magnitude 3 in Oklahoma more likely than not has a smaller magnitude than one above magnitude 3 randomly selected from the Parkfield region. // This is true. The smaller the b-value, the smaller the mean magnitude, which means that, given the earthquake magnitudes are exponentially distributed, the less likely you are to get a bigger earthquake. You can test this out with some hacker stats by making draws out of an Exponential distribution.
'''