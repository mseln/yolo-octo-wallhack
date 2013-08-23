import unittest
from tests import T1_unit, T2_unit, T3_unit


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(T1_unit.TestSequenceFunctions)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(T2_unit.TestArray)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(T3_unit.TestMath)

    all_tests = unittest.TestSuite([suite1, suite2, suite3])

    unittest.TextTestRunner(verbosity=2).run(all_tests)