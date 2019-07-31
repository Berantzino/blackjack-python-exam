from unittest import TestCase
from unittest.mock import patch
from unittest import main
from io import StringIO
import sys
import deck_of_cards
import player
import blackjack

class TestDeckOfCards(TestCase):

    ############################################################
    # Tests for Deck Class #####################################
    ############################################################
    def test_deck_len(self):
        deck = deck_of_cards.Deck()
        result = len(deck)
        self.assertEqual(result, 52)
    
    def test_deck_shuffle(self):
        deck1 = deck_of_cards.Deck()
        deck2 = deck_of_cards.Deck()
        deck2.shuffle()
        result = deck1 == deck2
        self.assertFalse(result)
    
    def test_deck_deal(self):
        deck = deck_of_cards.Deck()
        dealt_card = deck.deal()
        result = dealt_card not in deck.deck
        self.assertTrue(result)

    ############################################################
    # Tests for Card Class #####################################
    ############################################################
    def test_card_str(self):
        card = deck_of_cards.Card('Hearts', 'Ace')
        result = str(card)
        self.assertEqual(result, 'Ace of Hearts')


class TestPlayer(TestCase):

    ############################################################
    # Tests for Hand Class #####################################
    ############################################################
    def test_hand_add_card(self):
        hand1 = player.Hand()
        hand2 = player.Hand()
        card = deck_of_cards.Card('Hearts', 'Ace')
        hand2.add_card(card)
        result = hand1.cards == hand2.cards
        self.assertFalse(result)

    def test_hand_add_card_ace_counter(self):
        hand1 = player.Hand()
        hand1.add_card(deck_of_cards.Card('Hearts', 'Ace'))
        hand1.add_card(deck_of_cards.Card('Spades', 'Ace'))
        hand1.add_card(deck_of_cards.Card('Clubs', 'Ace'))
        result = hand1.aces
        self.assertEqual(result, 3)

    def test_hand_add_card_value_counter(self):
        hand1 = player.Hand()
        hand1.add_card(deck_of_cards.Card('Hearts', 'Ace'))
        hand1.add_card(deck_of_cards.Card('Spades', 'King'))
        result = hand1.value
        self.assertEqual(result, 21)

    def test_hand_adjust_for_ace(self):
        hand1 = player.Hand()
        hand1.add_card(deck_of_cards.Card('Diamonds', 'Ace'))
        hand1.add_card(deck_of_cards.Card('Spades', 'Ace'))
        hand1.adjust_for_ace()
        result = hand1.value
        self.assertEqual(result, 12)

    ############################################################
    # Tests for Chips Class ####################################
    ############################################################
    def test_chips_win_bet(self):
        chips = player.Chips(total=100)
        chips.bet = 50
        chips.win_bet()
        result = chips.total
        self.assertEqual(result, 150)
    
    def test_chips_lose_bet(self):
        chips = player.Chips(total=100)
        chips.bet = 50
        chips.lose_bet()
        result = chips.total
        self.assertEqual(result, 50)

class TestBlackjack(TestCase):

    @patch('builtins.input', return_value=50)
    def test_take_bet_valid_int(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        chips = player.Chips(total=100)
        blackjack.take_bet(chips)
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(chips.bet, 50)

    @patch('builtins.input', return_value=-50)
    def test_take_bet_negative_int(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        chips = player.Chips(total=100)
        blackjack.take_bet(chips)
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(chips.bet, 50)
    
    def test_hit(self):
        deck = deck_of_cards.Deck()
        hand = player.Hand()
        blackjack.hit(deck, hand)
        self.assertEqual(len(hand.cards), 1)
    
    @patch('builtins.input', return_value='Hit')
    def test_hit_or_stand_case_hit(self, input):
        deck = deck_of_cards.Deck()
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        blackjack.hit_or_stand(deck, player1)
        self.assertEqual(len(player1.hand.cards), 1)

    @patch('builtins.input', return_value='Stand')
    def test_hit_or_stand_case_stand(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        deck = deck_of_cards.Deck()
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        blackjack.hit_or_stand(deck, player1)
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(len(player1.hand.cards), 0)

    @patch('builtins.input', return_value=2)
    def test_play_as_dealer_true(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        result = blackjack.play_as_dealer()
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertTrue(result)

    @patch('builtins.input', return_value=1)
    def test_play_as_dealer_false(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        result = blackjack.play_as_dealer()
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertFalse(result)

    @patch('builtins.input', return_value=100)
    def test_deposit_valid_int(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        result = blackjack.deposit()
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, 100)

    @patch('builtins.input', return_value=-100)
    def test_deposit_negative_int(self, input):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        result = blackjack.deposit()
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, 100)

    def test_deal_initial_cards(self):
        deck = deck_of_cards.Deck()
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        computer1 = player.Player('Lasse', player.Hand(), player.Chips())
        blackjack.deal_initial_cards(deck, player1, computer1)
        self.assertEqual(len(player1.hand.cards), len(computer1.hand.cards))

    def test_reset_hands(self):
        deck = deck_of_cards.Deck()
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        computer1 = player.Player('Lasse', player.Hand(), player.Chips())
        blackjack.deal_initial_cards(deck, player1, computer1)
        blackjack.reset_hands(player1, computer1)
        result = len(player1.hand.cards) == 0 and len(computer1.hand.cards) == 0
        self.assertEqual(result, True)

    def test_check_winner_dealer_busts(self):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        dealer1 = player.Player('Lasse', player.Hand(), player.Chips())
        player1.hand.value, dealer1.hand.value = 15, 22
        blackjack.check_winner(player1, dealer1)
        result = captured_output.getvalue()
        expected_result = f'Dealer ({dealer1.name}) Busted - Player ({player1.name}) Won!\n'
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, expected_result)

    def test_check_winner_dealer_wins(self):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        dealer1 = player.Player('Lasse', player.Hand(), player.Chips())
        player1.hand.value, dealer1.hand.value = 15, 21
        blackjack.check_winner(player1, dealer1)
        result = captured_output.getvalue()
        expected_result = f'Dealer ({dealer1.name}) Won!\n'
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, expected_result)

    def test_check_winner_player_wins(self):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        dealer1 = player.Player('Lasse', player.Hand(), player.Chips())
        player1.hand.value, dealer1.hand.value = 21, 15
        blackjack.check_winner(player1, dealer1)
        result = captured_output.getvalue()
        expected_result = f'Player ({player1.name}) Won!\n'
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, expected_result)

    def test_check_winner_push(self):
        captured_output = StringIO()
        sys.stdout = captured_output # Redirects the output (print)
        player1 = player.Player('Lasse', player.Hand(), player.Chips())
        dealer1 = player.Player('Lasse', player.Hand(), player.Chips())
        player1.hand.value, dealer1.hand.value = 18, 18
        blackjack.check_winner(player1, dealer1)
        result = captured_output.getvalue()
        expected_result = f'Dealer ({dealer1.name}) and player ({player1.name}) tie! PUSH\n'
        sys.stdout = sys.__stdout__ # Resets the redirect
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    main()
