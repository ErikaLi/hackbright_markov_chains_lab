"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path)
    data = text.read()
    data = data.replace("\n", " ")

    return data


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
    words = text_string.split(" ")

    for i in xrange(len(words) - 1 - n):
        current_key = tuple(words[i : i + n])
        current_value = [words[i + n]]
        chains[current_key] = chains.get(current_key, []) + current_value


    return chains



def make_text(chains):
    """Return text from chains."""

    words = []
    # picking out random keys from a list of keys(from chains (tuples))
    ngrams = chains.keys()# lists
    random_key = choice(ngrams)#tuple
    #key_length = len(random_key)
    n = len(random_key)
    #push the first random key into words, use that in the loop
    words.extend(random_key)

    # loop until we cannot find a next word for the current key
    while chains.get(random_key):
        # find a list of possible next words of the current key
        possible_next_status = chains.get(random_key)
        # pick a word randomly from that list as our next word
        random_status = choice(possible_next_status)
        # append that word into our words list
        words.append(random_status)
        #print words
        # rebind the current key to be the last word of the key and the next word
        random_key = tuple(words[-n:])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 10)

# Produce random text
random_text = make_text(chains)

print random_text
