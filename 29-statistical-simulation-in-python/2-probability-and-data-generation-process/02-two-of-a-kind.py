'''
Two of a kind

Now let's use simulation to estimate probabilities. Suppose you've been invited to a game of poker at your friend's home. In this variation of the game, you are dealt five cards and the player with the better hand wins. You will use a simulation to estimate the probabilities of getting certain hands. Let's work on estimating the probability of getting at least two of a kind. Two of a kind is when you get two cards of different suites but having the same numeric value (e.g., 2 of hearts, 2 of spades, and 3 other cards).

By the end of this exercise, you will know how to use simulation to calculate probabilities for card games.
'''

import numpy as np

# Set random seed to get the same result or remove for different each time
np.random.seed(123)

# Deck of cards
deck_of_cards = []
cards, n_cards = ['Heart', 'Club', 'Spade', 'Diamond'], 13

for card in cards:
    deck_of_cards += list(zip([card]*n_cards, list(range(n_cards))))

'''
INSTRUCTIONS

*   In the for loop, shuffle deck_of_cards.
*   Utilize the get() method of a dictionary to count the number of occurrences of each card in the hand.
*   Increment the counter, two_kind, when there are at least two cards having the same numeric value in the hand.
'''

# Shuffle deck & count card occurrences in the hand
n_sims, two_kind = 10000, 0
for i in range(n_sims):
    np.random.shuffle(deck_of_cards)
    hand, cards_in_hand = deck_of_cards[0:5], {}
    for card in hand:
        # Use .get() method on cards_in_hand
        cards_in_hand[card[1]] = cards_in_hand.get(card[1], 0) + 1
    
    # Condition for getting at least 2 of a kind
    highest_card = max(cards_in_hand.values())
    if highest_card >= 2: 
        two_kind += 1

print("Probability of seeing at least two of a kind = {} ".format(two_kind/n_sims))