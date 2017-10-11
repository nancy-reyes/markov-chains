"""Generate Markov text from text files."""

from random import choice

import sys
import string

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_obj = open(file_path)
    contents = file_obj.read()
    file_obj.close()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.split()

    for i in range(len(text_string) - n):
        # we need to make bigram into a list that will be appended to
        # n times, and then turn the list into a tuple
        # list will have object i and loop n times.


        #ngram = (text_string[i], text_string[i + 1])
        # need to build a tuple containing n items. need to append to a list, and
        # then convert it to a tuple. a for loop that loops n times and appends
        # each word to the list.
        nlst = []

        for x in range(n):
            nlst.append(text_string[x + i])

        ngram = tuple(nlst)

        if ngram not in chains:
            chains[ngram] = [text_string[i+n]]
        else:
            chains[ngram].append(text_string[i+n])

    # second_last = text_string[-2]
    # last = text_string[-1]
    # last_ngram = (second_last,last)
    # chains[last_ngram] = None

    last_ngram = tuple(text_string[-n:])
    chains[last_ngram] = None

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []
    punctuation = ['.','?','!']

    # While true, if random_bigram's tuple starts with a capital letter, break
    # else choose a new random bigrram.

    random_bigram = choice(chains.keys())  # This is a tuple
    punct = set(string.punctuation)

    while True:  # Checks for capitalization and punctuation.
                 # otherwise, chooses a new ngram.
        if (random_bigram[0][0] == random_bigram[0][0].upper() and
            random_bigram[0][0] not in punct):
            break
        else:
            random_bigram = choice(chains.keys())

    # words.append(random_bigram)
    words = list(random_bigram)  # turns the random bigram into a list as starting pt.
    new_key = random_bigram  # reassigns the random ngram tuple to a new var

    while True:  # ends the program if it comes across the end of the paragraph or a word
                 # with a punctuation mark
        if chains[new_key] == None:
            break
        random_word = choice(chains[new_key])
        words.append(random_word)

        if random_word[-1] in punctuation:
            break

        # This creates the new key from the previous one.
        # This will be the old key, minus the first word, plus the random_word chosen.
        # ding = list(new_key)

        #THIS IS WHERE YOU LEFT OFF NANCY
        new_key = (new_key[1:n+1])
        print new_key

    # print chains[new_key]  # this is a LIST
    #for chain in chains:
    # new_key = (random_bigram[1], choice(chains[random_bigram]))
    # print random_bigram, new_key


    return " ".join(words)


input_path = sys.argv[1]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,3)

# Produce random text
random_text = make_text(chains)


print random_text

