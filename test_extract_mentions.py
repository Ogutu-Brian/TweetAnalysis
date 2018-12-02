"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_lower_case(self):
        """Non existence of upper case in mentions"""

        arg = 'The best gane is @SOccer'
        actual = tweets.extract_mentions(arg)
        expected = ['soccer']
        msg = "Expected {}, but returned {}".format(expected,actual)
        self.assertEqual(actual,expected,msg)

    def test_every_mention(self):
        """ Existence of all mentions within a tweet"""
        arg = '@george was a president. @george did a good job in his reign and now we have @klein'
        actual = tweets.extract_mentions(arg)
        expected = ['george','george','klein']
        msg = "Expected {}, but returned {}".format(expected,actual)
        self.assertEqual(actual,expected,msg)
    
    

if __name__ == '__main__':
    unittest.main(exit=False)
