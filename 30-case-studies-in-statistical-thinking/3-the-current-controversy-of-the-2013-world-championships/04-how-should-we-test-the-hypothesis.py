'''
How should we test the hypothesis?

You are interested in the presence of lane bias toward higher lanes, presumably due to a slight current in the pool. A natural null hypothesis to test, then, is that the mean fractional improvement going from low to high lane numbers is zero. Which of the following is a good way to simulate this null hypothesis?

As a reminder, the arrays swimtime_low_lanes and swimtime_high_lanes contain the swim times for lanes 1-3 and 6-8, respectively, and we define the fractional improvement as f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes.

INSTRUCTIONS

Possible Answers:

o   Randomly swap swimtime_low_lanes[i] and swimtime_high_lanes[i] with probability 0.5. From these randomly swapped arrays, compute the fractional improvement. The test statistic is the mean of this new f array. // This is simulating a different hypothesis, that whether a swimmer is in a high-numbered lane or a low-numbered lane has no bearing on the swim time. This is a perfectly reasonable hypothesis to test, but it is not the one we are testing here.
o   Scramble the entries in the swimtime_high_lanes, and recompute f from the scrambled array and the swimtime_low_lanes array. The test statistic is the mean of this new f array. // If you scramble one of the arrays of swim times, you are then comparing a swim of a high lane number and a swim of a low lane number for a different swimmer for a different stroke.
o   Shift the swimtime_low_lanes and swimtime_high_lanes arrays by adding a constant value to each so that the shifted arrays have the same mean. Compute the fractional improvement, f_shift, from these shifted arrays. Then, take a bootstrap replicate of the mean from f_shift. // This is simulating the hypothesis that averaging over all swimmers and strokes, the average swim time in high lanes is equal to that in low lanes. This is not the same as testing that the average fractional improvement is zero. We definitely want to test that the average fractional difference is zero because we want to normalize out differences in speed across strokes and gender.
*   Subtract the mean of f from f to generate f_shift. Then, take bootstrap replicate of the mean from this f_shift.
o   Either (3) or (4) will work; they are equivalent. // (3) and (4) are not equivalent. You can check this to computing the resulting shifted f, or by working it out with pen and paper.
'''

