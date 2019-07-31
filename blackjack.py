"""Blackjack Game

This script allows a player to play the game Blackjack.
"""

import deck_of_cards
import player as player_module
import ascii_msg

# Global variable to keep track of weither or not it is the player's turn
playing = True

def take_bet(chips):
    """Takes a bet from the player, based on text input and adds it to their chips.bet variable

    Parameters
    ----------
    chips : Chips
        The player's stack of chips
    """

    while True:
        try:
            chips.bet = abs(int(input('\nEnter the amount you would like to bet: ')))
        except ValueError:
            print('Your bet must be a whole number - Please try again')
            continue
        except:
            print('Error placing bet - Please try again')
            continue
        else:
            if chips.bet <= chips.total:
                print(f'\nYou have placed a bet of ${chips.bet}')
                break
            else:
                print(f'Insufficient Funds - You may not place a bet larger than ${chips.total}')
                continue

def hit(deck, hand):
    """Draws another card from the deck and places it in the player's hand

    Parameters
    ----------
    deck : Deck
        The deck provided by the dealer/game
    hand : Hand
        The player's hand object
    """

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, player):
    """Prompts the player to hit or stand

    Parameters
    ----------
    deck : Deck
        The deck provided by the dealer/game
    player : Player
        The player from which the action is required
    """

    global playing  # to control an upcoming while loop

    while True:

        action = input('\nHit/Stand? ')

        if action.lower() == 'hit':
            hit(deck, player.hand)
            break
        elif action.lower() == 'stand':
            print('+---------------+')
            print(f'| {player.name} Stands |')
            print('+---------------+')
            playing = False
            break
        else:
            print("\nPlease type 'Hit' or 'Stand' to continue the game.")
            continue

def show_some_cards(player, dealer):
    """Prints the player's two cards and one of the dealer's cards

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print('\n----------------------------------------')
    print(f"Dealer's Hand ({dealer.name}): {dealer.hand.CARD_VALUES[dealer.hand.cards[1].rank]}")
    print('This card is hidden')
    print(dealer.hand.cards[1])

    print(f"\nPlayer's Hand ({player.name}): {player.hand.value}")
    for card in player.hand.cards:
        print(card)
    print('----------------------------------------')

def show_all_cards(player, dealer):
    """Prints all the player's and dealer's cards

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in  the game
    """

    print('\n----------------------------------------')
    print(f"Dealer's Hand ({dealer.name}): {dealer.hand.value}")
    for card in dealer.hand.cards:
        print(card)

    print(f"\nPlayer's Hand ({player.name}): {player.hand.value}")
    for card in player.hand.cards:
        print(card)
    print('----------------------------------------')

def player_busts(player, dealer):
    """Prints that the player busted, the dealer won and adjusts chip balances accordingly

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print(f'Player ({player.name}) Busted  - Dealer ({dealer.name}) Won!')
    player.chips.lose_bet()
    dealer.chips.win_bet()

def player_wins(player, dealer):
    """Prints that the player won and adjusts chip balances accordingly

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print(f'Player ({player.name}) Won!')
    player.chips.win_bet()
    dealer.chips.lose_bet()

def dealer_busts(player, dealer):
    """Prints that the dealer busted, the player won and adjusts chip balances accordingly

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print(f'Dealer ({dealer.name}) Busted - Player ({player.name}) Won!')
    player.chips.win_bet()
    dealer.chips.lose_bet()

def dealer_wins(player, dealer):
    """Prints that the dealer won and adjusts chip balances accordingly

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print(f'Dealer ({dealer.name}) Won!')
    player.chips.lose_bet()
    dealer.chips.win_bet()

def push(player, dealer):
    """Prints that the game was a tie (PUSH)

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    print(f'Dealer ({dealer.name}) and player ({player.name}) tie! PUSH')

def play_as_dealer():
    """Asks the player if they want to play as the player or dealer

    Returns
    -------
    bool
        True if they want to play as the dealer, otherwise False
    """

    print('\nWho would you like to play as?')
    print('1. Player')
    print('2. Dealer')

    while True:
        try:
            choice = abs(int(input('')))
        except ValueError:
            print("Please provide the number '1' or '2'")
            continue
        except:
            print('Error getting input...')
            continue
        else:
            if choice > 2 or choice == 0:
                print("Please provide the number '1' or '2'")
                continue
            else:
                return choice == 2

def deposit():
    """Asks the player to deposit funds to their account

    Returns
    -------
    int
        The amount the player would like to deposit
    """

    while True:
        try:
            amount = abs(int(input('\nHow much would you like to deposit? ')))
        except ValueError:
            print('Please enter a whole number.')
            continue
        except:
            print('Error depositing funds...')
            continue
        else:
            print(f'\nYou have successfully deposited: ${amount}')
            return amount

def deal_initial_cards(deck, player, computer):
    """Deals the initial two cards to the player and the dealer and adjusts for aces

    Parameters
    ----------
    deck : Deck
        The deck provided by the dealer/game
    player : Player
        The player in the game
    computer : Player
        The computer in the game
    """

    player.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    player.hand.adjust_for_ace()

    computer.hand.add_card(deck.deal())
    computer.hand.add_card(deck.deal())
    computer.hand.adjust_for_ace()

def reset_hands(player, computer):
    """Resets the player's and computer's hands to prepair for a new game

    Parameters
    ----------
    player : Player
        The player in the game
    computer : Player
        The computer in the game
    """

    player.hand = player_module.Hand()
    computer.hand = player_module.Hand()

def check_winner(player, dealer):
    """Check the win conditions and calls the results function

    Parameters
    ----------
    player : Player
        The player in the game
    dealer : Player
        The dealer in the game
    """

    if dealer.hand.value > 21:
        dealer_busts(player, dealer)
    elif dealer.hand.value > player.hand.value:
        dealer_wins(player, dealer)
    elif dealer.hand.value < player.hand.value:
        player_wins(player, dealer)
    else:
        push(player, dealer)

def main():
    global playing
    # Prints a welcome message
    ascii_msg.welcome()

    # Asks for the player's desired display name
    player_name = input('\nEnter your display name: ')

    # Deposit Funds
    funds = deposit()

    # Asks if the the player would like to play as the dealer or the player
    choice = play_as_dealer()

    # Creates an object for the player and the computer
    bj_player = player_module.Player(player_name, player_module.Hand(), player_module.Chips(funds))
    bj_computer = player_module.Player('Computer', player_module.Hand(), player_module.Chips())

    while True:
        # if choice == False - Want to play as player
        if not choice:
            print('+-----------------------------------+')
            print('| You are now playing as the Player |')
            print('+-----------------------------------+')

            reset_hands(bj_player, bj_computer)

            deck = deck_of_cards.Deck()
            deck.shuffle()
            deal_initial_cards(deck, bj_player, bj_computer)

            take_bet(bj_player.chips)

            show_some_cards(bj_player, bj_computer)

            # Global variable set to True - False if the player stands
            while playing:

                hit_or_stand(deck, bj_player)

                show_some_cards(bj_player, bj_computer)

                # If player's hand exceeds 21, player_busts() is called and we break the while loop
                if bj_player.hand.value > 21:
                    player_busts(bj_player, bj_computer)
                    break

            # If the player hasn't busted, the dealer's hand is played until it reaches 17 or above
            # Dealer will Stand on 17 and above
            if bj_player.hand.value <= 21:

                while bj_computer.hand.value < 17:
                    hit(deck, bj_computer.hand)

                show_all_cards(bj_player, bj_computer)

                check_winner(bj_player, bj_computer)

            # Informs the player of their total amount of chips
            print(f'\nYour total chips are at: {bj_player.chips.total}')

            new_game = input('\nWould you like to play again? y/n: ')

            if new_game.lower() == 'y':
                playing = True
                print('\n' * 100)
                continue
            else:
                print('\n' * 100)
                ascii_msg.goodbye()
                break

        # else (choice == True) - Want to play as dealer
        else:
            print('+-----------------------------------+')
            print('| You are now playing as the Dealer |')
            print('+-----------------------------------+')

            reset_hands(bj_player, bj_computer)

            deck = deck_of_cards.Deck()
            deck.shuffle()
            deal_initial_cards(deck, bj_player, bj_computer)

            take_bet(bj_player.chips)

            # Show all cards (possible since the player is playing automatically)
            show_all_cards(bj_computer, bj_player)

            while True:

                # Auto-play logic here
                # The computer will hit on 4-15 and stand on 16-21
                if bj_computer.hand.value > 15 and bj_computer.hand.value <= 21:
                    print('+---------------+')
                    print(f'| {bj_computer.name} Stands |')
                    print('+---------------+')
                    break
                else:
                    hit(deck, bj_computer.hand)

                show_all_cards(bj_computer, bj_player)

                # If player's hand exceeds 21, run player_busts() and break out of loop
                if bj_computer.hand.value > 21:
                    player_busts(bj_computer, bj_player)
                    break

            # If computer hasn't busted, the Dealer's hand will be played
            if bj_computer.hand.value <= 21:

                while playing:

                    # Dealer auto stands at 17, 18, 19, 20, 21
                    if bj_player.hand.value >= 17 and bj_player.hand.value <= 21:
                        playing = False
                        break
                    
                    hit_or_stand(deck, bj_player)

                    show_all_cards(bj_computer, bj_player)

                    if bj_player.hand.value > 21:
                        playing = False

                check_winner(bj_computer, bj_player)

            # Inform Player of their chips total
            print(f'\nYour total chips are at: {bj_player.chips.total}')

            new_game = input('\nWould you like to play again? y/n: ')

            if new_game.lower() == 'y':
                playing = True
                print('\n' * 100)
                continue
            else:
                print('\n' * 100)
                ascii_msg.goodbye()
                break

if __name__ == "__main__":
    main()
