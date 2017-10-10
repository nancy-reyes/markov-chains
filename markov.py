"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_obj = open(file_path)
    contents = file_obj.read()
    file_obj.close()

    return contents


def make_chains(text_string):
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

    for i in range(len(text_string) - 2):
        bigram = (text_string[i], text_string[i + 1])
        
        if bigram not in chains:
            chains[bigram] = [text_string[i+2]]
        else:
            chains[bigram].append(text_string[i+2])

    second_last = text_string[-2]
    last = text_string[-1]
    last_bigram = (second_last,last)
    chains[last_bigram] = None

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    random_bigram = choice(chains.keys())  # This is a tuple
    # words.append(random_bigram)
    words = list(random_bigram)
    new_key = random_bigram

    while True:
        if chains[new_key] == None:
            break
        random_word = choice(chains[new_key]) 
        words.append(random_word)
        new_key  = (new_key[1],random_word)

    # print chains[new_key]  # this is a LIST
    #for chain in chains:
    # new_key = (random_bigram[1], choice(chains[random_bigram]))
    # print random_bigram, new_key


    return " ".join(words)


input_path = "dtspeeches.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)


print random_text

