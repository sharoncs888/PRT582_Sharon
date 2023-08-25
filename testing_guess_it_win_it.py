"""
Unit tests Guess_it_Win_it
"""

import unittest
from guess_it_win_it import Game


class TestGameGuessItWinIt(unittest.TestCase):
    """
    Unit tests for the Game class in Guess_it_Win_it
    """
    def setUp(self):
        self.guessitwinit = Game()

    def test_input_testcase(self):
        """Test input functions that take values from the user"""
        self.guessitwinit.user_input = '1111'
        self.assertTrue(self.guessitwinit.verify_entry(self.guessitwinit.user_input))

        self.guessitwinit.user_input = 'Wrongentry'
        self.assertFalse(self.guessitwinit.verify_entry(self.guessitwinit.user_input))
        print("Unit Test case user entry functions: Passed")

    def test_random_generation_testcase(self):
        """Test whether the randomly generated number is valid for the game"""
        random_number = self.guessitwinit.random_generator()
        self.assertTrue(1000 <= random_number <= 9999)
        print("Unit Test case Random Number generation: Passed ")

    def test_datatype_testcase(self):
        """Test and verify data types"""
        self.assertTrue(isinstance(self.guessitwinit.hint_out(1234), list))
        self.assertTrue(isinstance(self.guessitwinit.tries, int))
        self.assertTrue(isinstance(self.guessitwinit.original, int))
        print("Unit Test case datatypes: Passed")

    def test_hint_out_testcase(self):
        """Test the hint given out to the user"""
        user_input = "1243"
        hints = self.guessitwinit.hint_out(user_input)
        self.assertTrue(all(item in ['x', 'o'] for item in hints))
        print("Unit Test case function hint_out: Passed")


if __name__ == '__main__':
    unittest.main()
