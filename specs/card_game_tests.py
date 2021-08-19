
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):

        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("hearts", 7)
        self.cards = [self.card_1, self.card_2]
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card_1))

    def test_highest_card(self):
        self.assertEqual(self.card_2, self.cardgame.highest_card(self.card_1, self.card_2))

    def test_card_total(self):
        self.assertEqual("You have a total of 8", self.cardgame.card_total(self.cards))

