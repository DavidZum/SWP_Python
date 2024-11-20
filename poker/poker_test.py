import unittest
from poker import Card, is_straight, is_same_color


class TestPoker(unittest.TestCase):
    def setUp(self):
        self.straight = [
            Card('3', '♣'),
            Card('4', '♠'),
            Card('5', '♦'),
            Card('6', '♥'),
            Card('7', '♠')
        ]
        
        self.flush = [
            Card('J', '♥'),
            Card('6', '♥'),
            Card('9', '♥'),
            Card('Q', '♥'),
            Card('K', '♥')
        ]
    
    
    def test_is_straight(self):
        self.assertTrue(is_straight(self.straight))
        self.assertFalse(is_straight(self.flush))

    def test_is_same_color(self):
        self.assertTrue(is_same_color(self.flush))
        self.assertFalse(is_same_color(self.straight))
if __name__ == '__main__':
    unittest.main()