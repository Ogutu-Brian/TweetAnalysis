"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """

    # TODO: complete this function body


# TODO: Add the remaining Assignment 3 functions below.


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
