"""
Contains classes Player, Hand and Chips
"""

class Player():
    """
    A class used to represent a player/computer playing blackjack

    ...

    Attributes
    ----------
    name : str
        the name of the player
    hand : Hand
        a hand object with the player's' cards
    chips : Chips
        a chips object with the player's chip total and bet amount
    """

    def __init__(self, name, hand, chips):
        self.name = name
        self.hand = hand
        self.chips = chips

class Hand():
    """
    A class used to represent a player's hand of cards

    ...

    Attributes
    ----------
    cards : list
        a list of the player's cards
    value : int
        the numerical value of the player's cards
    aces : int
        the amount of aces the player holds

    Methods
    -------
    add_card(card)
        adds a card to the player's list of cards, the value of it and ups the ace counter if needed
    adjust_for_aces()
        adjusts the value of an ace from 11 to 1 if needed 11 would force a bust
    """

    CARD_VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                   'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

        if card.rank == 'Ace':
            self.aces += 1

        self.value += self.CARD_VALUES[card.rank]

    def adjust_for_ace(self):
        # 0 is treated as False
        # 1,2,3 etc. is treated as true
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    """
    A class used to represent a player's stack of chips

    ...

    Attributes
    ----------
    total : int
        the player's chip balance
    bet : int
        the bet amount placed by the player

    Methods
    -------
    win_bet()
        adds the bet to the player's total amount of chips, if bet was won
    lose_bet()
        deducts the bet from the player's total amount of chips, the the bet was lost

    """

    def __init__(self, total=0):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
