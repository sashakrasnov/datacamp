'''
Driving test

Through the next exercises, we will learn how to build a data generating process (DGP) through progressively complex examples.

In this exercise, you will simulate a very simple DGP. Suppose that you are about to take a driving test tomorrow. Based on your own practice and based on data you have gathered, you know that the probability of you passing the test is 90% when it's sunny and only 30% when it's raining. Your local weather station forecasts that there's a 40% chance of rain tomorrow. Based on this information, you want to know what is the probability of you passing the driving test tomorrow.

This is a simple problem and can be solved analytically. Here, you will learn how to model a simple DGP and see how it can be used for simulation.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Deck of cards
deck = []
cards, n_cards = ['Heart', 'Club', 'Spade', 'Diamond'], 13

for card in cards:
    deck += list(zip([card]*n_cards, list(range(n_cards))))

'''
INSTRUCTIONS 1/2

*   Write a function test_outcome() to simulate the weather.
    *   Set weather as 'rain' or 'sun' depending on the input argument p_rain (the probability of rain).
    *   Based on the weather, return 'pass' or 'fail'.
'''

sims, outcomes, p_rain, p_pass = 1000, [], 0.40, {'sun':0.9, 'rain':0.3}

def test_outcome(p_rain):
    # Simulate whether it will rain or not
    weather = np.random.choice(['rain', 'sun'], p=[p_rain, 1-p_rain])
    # Simulate and return whether you will pass or fail
    return np.random.choice(['pass', 'fail'], p=[p_pass[weather], 1-p_pass[weather]])

'''
INSTRUCTIONS 2/2

*   Compute the probability of passing the test. You'll have to count the number of times you pass the test, as collected in outcomes.
'''

for _ in range(sims):
    outcomes.append(test_outcome(p_rain))

# Calculate fraction of outcomes where you pass
print("Probability of Passing the driving test = {}".format(outcomes.count('pass')/sims))