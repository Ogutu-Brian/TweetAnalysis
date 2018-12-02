"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple
import operator

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
    mentions = []
    for i in range(len(text)):
        if text[i] == MENTION_SYMBOL:
            mentions.append(first_alnum_substring(text[i+1:]))
    return mentions

def extract_hashtags(text: str) -> List[str]:
    """Return a list of all unique hashtags in text, in the order in which they appear
    in text, converted to lowercase. 
    
    @type text:str
    @rtype: list
    
    >>> etract_hashtag('In #December we have #christmas')
    ['december','christmas']
    >>> extract_hashtag('learning python #code is essential in #Introduction to #CODE')
    ['code','introduction','code']
    """

    hash_tags = []
    for i in range(len(text)):
        if text[i+1] == HASH_SYMBOL:
            word = first_alnum_substring(text[i+1:])
            if word not in hash_tags:
                hash_tags.append(word)
    return hash_tags
            
def count_words(text: str,count_dict:Dict[str,int]) -> None:
    """Updates counts of words in the dictionary.
    If a word is not in the dictionary yet it is added and returns None
    
    @type text:str
    @type count_dict:Dict[str,int]
    @rtype: Node

    >>> count_dict = {}
    >>> count_words('This is a Simple? tweet and a nice one',count_dict)
    >>> 
    """

    word_list = [clean_word(word) for word in text.split(" ")]

    for word in word_list:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return None

def common_words(count_dict:Dict[str,int],N:int) -> None:
    """Updates a dictionary so that it only includes the most common words.
    At most N words should be kept in the dictionary.

    @type count_dict:Dict[str:int]
    @type N: int
    @rtype: None

    >>> count_dict = {}
    >>> common_words(count_dict,2)
    >>>
    """
    sorted_collection = []
    sorted_list = sorted(count_dict.values(),reverse=True)
    for value in sorted_list:
        for key in count_dict:
            if count_dict[key] == value:
                sorted_collection.append((key,value))
    
    end_index = N-1
    if len(sorted_collection) == 0 or len(sorted_collection) == 1:
        return None
    else:
        while end_index < len(sorted_collection) - 1:
            if sorted_collection[end_index][1] != sorted_collection[end_index + 1][1]:
                sorted_collection = sorted_collection[0:end_index + 1]
                break
            else:
                end_index -= 1
                
    count_dict.clear()
    for item in sorted_collection:
        count_dict[item[0]] = item[1]
    return None

def read_tweets(file: TextIO) -> Dict[str,List[tuple]]:
    file = open("tweets_smnall.txt")
    
if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
