'''
Full house

Let's return to our poker game. Last time, we calculated the probability of getting at least two of a kind. This time we are interested in a full house. A full house is when you get two cards of different suits that share the same numeric value and three other cards that have the same numeric value (e.g., 2 of hearts & spades, jacks of clubs, diamonds, & spades).

Thus, a full house is the probability of getting exactly three of a kind conditional on getting exactly two of a kind of another value. Using the same code as before, modify the success condition to get the desired output. This exercise will teach you to estimate conditional probabilities in card games and build your foundation in framing abstract problems for simulation.
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
INSTRUCTIONS

*   Shuffle deck_of_cards.
*   Utilize a dictionary with .get() to count the number of occurrences of each card in the hand.
*   Increment the counter full_house when there is a full house in the hand (2 of one kind, 3 of the other).
'''

#Shuffle deck & count card occurrences in the hand
n_sims, full_house, deck_of_cards = 50000, 0, deck.copy() 
for i in range(n_sims):
    np.random.shuffle(deck_of_cards)
    hand, cards_in_hand = deck_of_cards[0:5], {}
    for card in hand:
        # Use .get() method to count occurrences of each card
        cards_in_hand[card[1]] = cards_in_hand.get(card[1], 0) + 1
        
    # Condition for getting full house
    condition = (max(cards_in_hand.values()) == 3) & (min(cards_in_hand.values())==2)
    if  condition == True: 
        full_house += 1
print("Probability of seeing a full house = {}".format(full_house/n_sims))