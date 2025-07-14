# WRITE YOUR CODE HERE
import unittest
from src.game import calculate_new_score

class TestGameLogic(unittest.TestCase):
    def test_calculate_new_score(self):
        self.assertEqual(calculate_new_score(100, 50), 150)

if __name__ == '__main__':
    unittest.main()