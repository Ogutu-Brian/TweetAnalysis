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
        if i < len(text)-2 and text[i+1] == HASH_SYMBOL:
            word = first_alnum_substring(text[i+1:])
            if word not in hash_tags:
                hash_tags.append(word)
    return hash_tags


def count_words(text: str, count_dict: Dict[str, int]) -> None:
    """Updates counts of words in the dictionary.
    If a word is not in the dictionary yet it is added and returns None
    @type text:str
    @type count_dict:Dict[str,int]
    @rtype: Node
    >>> count_dict = {}
    >>> count_words('This is a Simple? tweet and a nice one',count_dict)
    >>>
    """
    text_list = [word for word in text.split(" ")]
    for word in text_list:
        if word[0] == HASH_SYMBOL or word[0] == MENTION_SYMBOL:
            text_list.remove(word)
    word_list = [clean_word(word) for word in text_list]
    for word in word_list:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] = count_dict[word] + 1


def common_words(count_dict: Dict[str, int], number: int) -> None:
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
    sorted_list = sorted(count_dict.values(), reverse=True)
    for value in sorted_list:
        for key in count_dict:
            if count_dict[key] == value:
                sorted_collection.append((key, value))
    end_index = number-1
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


def read_tweets(file: TextIO) -> Dict[str, List[tuple]]:
    """Takes input from a file and processes it into a dictionary of
    tweets
    """
    file_content = file.readlines()
    file_content = list(filter(None, file_content))
    content_dict = {}
    keys = []
    for line in file_content:
        if len(line) > 0 and line[len(line) - 2] == ":":
            keys.append(line.lower())
    for key in keys:
        content_dict[key] = []
        index = 0
        for line in file_content:
            if line.lower() not in keys:
                content_dict[key].append(line)
            elif line.lower() in keys and len(content_dict[key]) > 0:
                break
            index += 1
        del file_content[0:index + 1]
    return tweet_tuple(content_dict)


def tweet_tuple(content_dict: Dict[str, List[str]]) -> Dict[str, List[tuple]]:
    """Returns a dictionary of tweets in an ordered format
    @type content_dict: Dict[str, List[str]]
    @rtype: Dict[str, List[tuple]]
    """
    tweet_dict = {}
    for key in content_dict:
        item = content_dict[key]
        info = item[0].split(',')
        tweet_text = (','.join(item[1:])).rstrip().split("<<<EOT")
        tweet_tupple = (tweet_text, int(info[0]), info[2],
                        int(info[3]), int(info[4]))
        tweet_dict[key.rstrip()] = list(tweet_tupple)
    return tweet_dict


def most_popular(read_tweets_dict: Dict[str, List[tuple]],
                 date_1: int, date_2: int) -> str:
    """Returns username of twitter user who was most popular on twitter
    between date_1 and date_2
    @type read_dict_tweets_dict: Dict[str, List[tupple]]
    @type date_1: int
    @type date_2: int
    @rtype: str
    """
    keys = []
    for key in read_tweets_dict.keys():
        if read_tweets_dict[key][0][TWEET_DATE_INDEX] in range(date_1, date_2 + 1):
            keys.append(key)
    if len(keys) == 0:
        return "tie"
    largest_key = keys[0]
    is_multiple = False
    count = 1
    while count < len(keys):
        key = keys[count]
        if ((popularity(key, read_tweets_dict))
                >= (popularity(largest_key, read_tweets_dict))):
                is_multiple = ((popularity(key, read_tweets_dict))
                               == (popularity(largest_key, read_tweets_dict)))
                largest_key = key
        count += 1
    if is_multiple:
        return "tie"
    return largest_key


def popularity(key: str, read_tweets_dict: Dict[str, List[tuple]]) -> int:
    """Returns the popularity of a given user depending on the key
    in the dictionary
    @type key: str
    @type read_tweets_dict: Dict[str,List[tuple]]
    @rtype; int
    """
    return read_tweets_dict[key][0][TWEET_FAVOURITE_INDEX] +\
        read_tweets_dict[key][0][TWEET_RETWEET_INDEX]


def detect_author(read_tweets_dict: Dict[str, List[tuple]], text: str) -> str:
    """Returns an author of a tween dpending on the frequency of times 
    a given user uses an ashtag
    @type read_tweets_dict: Dict[str,List[tuple]]
    @type text: str
    @rtype: str
    """
    keys = list(read_tweets_dict.keys())
    leading_key = keys[0]
    largest_number = 0
    for tweet in read_tweets_dict[leading_key][0][0]:
        largest_number += extract_hashtags(tweet).count(text)
    count = 1
    while count < len(keys):
        key = keys[count]
        number = 0
        for tweet in read_tweets_dict[key][0][0]:
            number += extract_hashtags(tweet).count(text)
        if number > largest_number:
            leading_key = key
            largest_number = number
        count += 1
    if largest_number == 0:
        return "unknown"
    return leading_key


if __name__ == '__main__':
    pass
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
