'''
Game of thirteen

A famous French mathematician Pierre Raymond De Montmart, who was known for his work in combinatorics, proposed a simple game called as Game of Thirteen. You have a deck of 13 cards, each numbered from 1 through 13. Shuffle this deck and draw cards one by one. A coincidence is when the number on the card matches the order in which the card is drawn. For instance, if the 5th card you draw happens to be a 5, it's a coincidence. You win the game if you get through all the cards without any coincidences. Let's calculate the probability of winning at this game using simulation.

By completing this exercise, you will further strengthen your ability to cast abstract problems into the simulation framework for estimating probabilities.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(111)

'''
INSTRUCTIONS

*   For each drawing, draw all the cards in deck without replacement and assign to draw.
*   Check if there are any coincidences in the draw and, if there are, increment the coincidences counter by 1.
*   Calculate winning probability as the fraction of games without any coincidences.
'''

# Pre-set constant variables
deck, sims, coincidences = np.arange(1, 14), 10000, 0

for _ in range(sims):
    # Draw all the cards without replacement to simulate one game
    draw = np.random.choice(a=deck, size=len(deck), replace=False)
    # Check if there are any coincidences
    coincidence = (draw == list(np.arange(1, 14))).any()
    
    if coincidence == True: 
        coincidences += 1

# Calculate probability of winning
print("Probability of winning = {}".format(1-coincidences/sims))
