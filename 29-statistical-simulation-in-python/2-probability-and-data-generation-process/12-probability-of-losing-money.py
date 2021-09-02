'''
Probability of losing money

In this exercise, we will use the DGP model to estimate probability.

As seen earlier, this company has the option of spending extra money, let's say $3000, to redesign the ad. This could potentially get them higher clickthrough and signup rates, but this is not guaranteed. We would like to know whether or not to spend this extra $3000 by calculating the probability of losing money. In other words, the probability that the revenue from the high-cost option minus the revenue from the low-cost option is lesser than the cost.

Once we have simulated revenue outcomes, we can ask a rich set of questions that might not have been accessible using traditional analytical methods.

This simple yet powerful framework forms the basis of Bayesian methods for getting probabilities.
'''

import numpy as np

def get_signups(cost, ct_rate, su_rate, sims):
    lam = np.random.normal(loc=100000, scale=2000, size=sims)
    # Simulate impressions(poisson), clicks(binomial) and signups(binomial)
    impressions = np.random.poisson(lam=lam)
    clicks = np.random.binomial(impressions, p=ct_rate[cost])
    signups = np.random.binomial(clicks, p=su_rate[cost])
    return signups


def get_revenue(signups):
    rev = []
    np.random.seed(123)
    for s in signups:
        # Model purchases as binomial, purchase_values as exponential
        purchases = np.random.binomial(s, p=0.1)
        purchase_values = np.random.exponential(size=purchases, scale=1000)
        
        # Append to revenue the sum of all purchase values.
        rev.append(sum(purchase_values))
    return rev


# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Initialize click-through rate and signup rate dictionaries
ct_rate = {'low':0.01, 'high':np.random.uniform(low=0.01, high=1.2*0.01)}
su_rate = {'low':0.20, 'high':np.random.uniform(low=0.20, high=1.2*0.20)}

'''
INSTRUCTIONS

*   Initialize cost_diff, the difference between the 'high' and 'low' cost options, to 3000.
*   Get the revenue for the high-cost option and assign it to rev_high.
*   Calculate the fraction of times when rev_high - rev_low is less than cost_diff.
'''

# Initialize cost_diff
sims, cost_diff = 10000, 3000

# Get revenue when the cost is 'low' and when the cost is 'high'
rev_low = get_revenue(get_signups('low', ct_rate, su_rate, sims))
rev_high = get_revenue(get_signups('high', ct_rate, su_rate, sims))

# calculate fraction of times rev_high - rev_low is less than cost_diff
print("Probability of losing money = {}".format(sum(np.array(rev_high)-np.array(rev_low)<cost_diff)/sims))