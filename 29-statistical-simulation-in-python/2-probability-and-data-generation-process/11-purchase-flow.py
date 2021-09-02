'''
Purchase Flow

After signups, let's model the revenue generation process. Once the customer has signed up, they decide whether or not to purchase - a natural candidate for a binomial RV. Let's assume that 10% of signups result in a purchase.

Although customers can make many purchases, let's assume one purchase. The purchase value could be modeled by any continuous RV, but one nice candidate is the exponential RV. Suppose we know that purchase value per customer has averaged around $1000. We use this information to create the purchase_values RV. The revenue, then, is simply the sum of all purchase values.

The variables ct_rate, su_rate and the function get_signups() from the last exercise are pre-loaded for you.
'''

import numpy as np

def get_signups(cost, ct_rate, su_rate, sims):
    lam = np.random.normal(loc=100000, scale=2000, size=sims)
    # Simulate impressions(poisson), clicks(binomial) and signups(binomial)
    impressions = np.random.poisson(lam=lam)
    clicks = np.random.binomial(impressions, p=ct_rate[cost])
    signups = np.random.binomial(clicks, p=su_rate[cost])
    return signups


# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Initialize click-through rate and signup rate dictionaries
ct_rate = {'low':0.01, 'high':np.random.uniform(low=0.01, high=1.2*0.01)}
su_rate = {'low':0.20, 'high':np.random.uniform(low=0.20, high=1.2*0.20)}

'''
INSTRUCTIONS

*   Model purchases as a binomial RV with p=0.1.
*   Model purchase_values as an exponential RV scale=1000 and the appropriate size.
*   Append rev with the sum of purchase_values.
'''

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

print("Simulated Revenue = ${}".format(get_revenue(get_signups('low', ct_rate, su_rate, 1))[0]))