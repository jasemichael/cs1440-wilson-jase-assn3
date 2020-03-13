import unittest
from src.Card import Card
from src.NumberSet import NumberSet

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(0, 3, NumberSet(18))
        self.card1 = Card(0, 0, NumberSet(0))


    def test_getSize(self):
        self.assertEqual(self.card.getSize(), 3)
        self.assertEqual(self.card1.getSize(), 0)

    def test_getID(self):
        self.assertIsNotNone(self.card)
        self.assertIsNotNone(self.card1)
        self.assertEqual(self.card.getId(), 0)
        self.assertEqual(self.card1.getId(), 0)



if __name__ == '__main__':
    unittest.main()

