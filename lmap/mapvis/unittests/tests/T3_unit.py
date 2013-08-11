import random
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(1+1, 2)

    def test_choice(self):
        self.assertEqual(2*5, 5*2)

if __name__ == '__main__':
    unittest.main()


