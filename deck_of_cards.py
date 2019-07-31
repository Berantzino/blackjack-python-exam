"""
Contains classes Deck and Card
"""

import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')

class Deck():
    """
    A class used to represent a deck of cards

    ...

    Attributes
    ----------
    deck : list
        a list containing Card objects

    Methods
    -------
    __str__()
        returns a formatted string of what cards the deck contains
    __len__()
        returns the amount cards in the deck
    shuffle()
        randomly shuffles the cards in the deck list
    deal()
        returns a random card from the deck
    """

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit=suit, rank=rank))

    def __str__(self):
        deck_string = '\nThe Deck Contains:\n'
        for card in self.deck:
            deck_string += str(card) + '\n'

        return deck_string

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

class Card():
    """
    A class used to represent a playing card

    ...

    Attributes
    ----------
    suit : str
        a cards suit (Hearts, Diamonds, Spades, Clubs)
    rank : str
        a cards rank (Two, Three, ..., Ace)

    Methods
    -------
    __str__()
        returns a formatted string representation of a card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
