import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp (self):
        self.card1 = Card("Hearts", 8)
        self.card2 = Card("Spades", 5)
        self.card3 = Card ("Clubs", 1)
        self.cardgame = CardGame()
        self.cards = [self.card1, self.card2, self.card3]


    def test_card_value_is_not_ace (self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card1))
    
    def test_card_value_is_ace (self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card3))

    def test_which_card_is_higher(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self.card1, self.card2) )

    def test_find_cards_total (self):
        self.assertEqual("You have a total of" + "14",  self.cardgame.cards_total(self.cards))
