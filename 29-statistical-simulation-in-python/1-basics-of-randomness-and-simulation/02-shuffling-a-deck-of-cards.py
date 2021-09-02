'''
Shuffling a deck of cards

Often times we are interested in randomizing the order of a set of items. Consider a game of cards where you first shuffle the deck of cards or a game of scrabble where the letters are first mixed in a bag. As the final exercise of this section, you will learn another useful function - np.random.shuffle(). This function allows you to randomly shuffle a sequence in place. At the end of this exercise, you will know how to shuffle a deck of cards or any sequence of items.

Examine deck_of_cards in the shell.
'''

import numpy as np

deck_of_cards = []
cards, n_cards = ['Heart', 'Club', 'Spade', 'Diamond'], 13

for card in cards:
    deck_of_cards += list(zip([card]*n_cards, list(range(n_cards))))

'''
INSTRUCTIONS

*   Use the np.random.shuffle() function to shuffle this deck of cards.
*   Select the top three cards from this list by slicing.
'''

# Shuffle the deck
np.random.shuffle(deck_of_cards)

# Print out the top three cards
card_choices_after_shuffle = deck_of_cards[:3]
print(card_choices_after_shuffle)