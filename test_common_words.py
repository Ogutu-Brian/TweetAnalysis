"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """

    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_most_common_only(self):
        """Dictionary with varied number of frequencies"""

        arg1 = {"hello":2,"try":5,"count":1,"val":8}
        arg2 = 2
        exp_arg1 = {"val":8,"try":5}
        act_return = tweets.common_words(arg1,arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
    
    def test_frequency_repetition(self):
        """Dictionary with repeated frequencies"""
        arg1 = {"man":5,"boy":2,"ken":5,"hilbert":7}
        arg2 = 2
        exp_arg1 = {"hilbert":7}
        act_return = tweets.common_words(arg1,arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)

if __name__ == '__main__':
    unittest.main(exit=False)
