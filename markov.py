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
    words = open_and_read_file("green-eggs.txt").split(" ")

    for i in xrange(len(words) - 3):
        current_key = (words[i], words[i + 1])
        current_value = [words[i + 2]]
        chains[current_key] = chains.get(current_key, []) + current_value


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    pairs = chains.keys()
    random_key = choice(pairs)
    words.extend(list(random_key))

    while chains.get(random_key) is not None:
        possible_next_status = chains.get(random_key)
        random_status = choice(possible_next_status)
        words.append(random_status)
        random_key = (words[-2], words[-1])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
