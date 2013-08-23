import random
import unittest

def get(a, i):
    return a[i]

class TestArray(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    
    def test_index(self):
        # should raise an exception for out of range
        self.assertRaises(IndexError, get, self.seq, 10)

    def test_size(self):
        self.assertEqual(len(self.seq), 10)

if __name__ == '__main__':
    unittest.main()