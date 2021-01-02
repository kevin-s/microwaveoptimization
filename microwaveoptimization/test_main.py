import unittest

from microwaveoptimization import main


class MyTestCase(unittest.TestCase):
    def test_thirtySecondIncrements_givenThirty_shouldReturnOne(self):
        actual = main.thirtySecondIncrements(30)
        self.assertEqual(1, actual)

    def test_thirtySecondIncrements_givenTwentyFive_shouldReturnNone(self):
        actual = main.thirtySecondIncrements(25)
        self.assertEqual(None, actual)

    def test_thirtySecondIncrements_givenSixty_shouldReturnTwo(self):
        actual = main.thirtySecondIncrements(60)
        self.assertEqual(2, actual)


if __name__ == '__main__':
    unittest.main()
