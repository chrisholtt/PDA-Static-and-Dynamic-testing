import unittest
from src.card import Card
from src.card_game import CardGame



class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Clubs", 4)
        self.card2 = Card("Spades", 1)

        self.cards = [
            self.card1,
            self.card2
        ]
    
    def test_card_is_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card1, CardGame.highest_card(self, self.card1, self.card2))

    def test_total_cards(self):
        self.assertEqual("You have a total of 5", CardGame.cards_total(self, self.cards))