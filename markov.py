"""Generate Markov text from text files."""

from random import choice
from string import punctuation
import sys
import markovtweets


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path)
    data = text.read()
    data = data.replace("\n", " ")
    data = data.replace(" -- ","")
    data = data.replace("  "," ")

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
    # key_length = len(random_key)
    n = len(random_key)
    # push the first random key into words
    words.extend(random_key)

    # until we cannot find a next word for the current key
    while chains.get(random_key):
        # find a list of possible next words of the current key
        possible_next_status = chains.get(random_key)
        # pick a word randomly from that list
        random_status = choice(possible_next_status)
        # append that word into our words list
        words.append(random_status)
        # rebind the current key to be the last word of the key and the next word
        random_key = tuple(words[-n:])

    return " ".join(words)


def capitalise_punctuate(chains):
    """return a sentence with a capitalised beginning and punctuated ending"""

    words = []
    # picking out random keys from a list of keys(from chains (tuples))
    ngrams = chains.keys()  # lists
    # ref : https://stackoverflow.com/questions/7100243/finding-in-elements-in-a-tuple-and-filtering-them

    capitalised_ngrams = [ngram for ngram in ngrams if ngram[0][0] == ngram[0][0].upper()]
    random_key = choice(capitalised_ngrams)  # tuple
    # key_length = len(random_key)
    n = len(random_key)
    # push the first random key into words, use that in the loop
    words.extend(random_key)

    # loop until we cannot find a next word for the current key
    while chains.get(random_key):
        # find a list of possible next words of the current key
        possible_next_status = chains.get(random_key)
        # pick a word randomly from that list as our next word
        random_status = choice(possible_next_status)
        # append that word into our words list
        words.append(random_status)
        if words[-1][-1] in punctuation:
            break
        # rebind the current key to be the last word of the key and the next word
        random_key = tuple(words[-n:])

    return " ".join(words)


def limit_chars(max_length):
    tweets = ""
    while len(tweets) <= max_length:
        new_tweet = tweets + " " + capitalise_punctuate(chains)
        if len(new_tweet) > max_length:
            return tweets
        tweets = tweets + " " + capitalise_punctuate(chains)

    return tweets



def retweet():
    feed = markovtweets.update(limit_chars(140))
    decision = raw_input("Enter to tweet again [q to quit] >")
    if decision == "":
        feed = markovtweets.update(limit_chars(140))
        decision = raw_input("Enter to tweet again [q to quit] >")
    else:
        print "thanks for tweeting"



# def cast(file_path):
#     """Parse the file into dictionary with characters as keys and string of their lines as values"""

#     characters = []
#     all_dialogue = []
#     cast = {}
#     text = open(file_path)
#     data = text.read()
#     data = data.replace(" -- ","")
#     data = data.replace("  "," ")
#     all_dialogues = data.split("\n")

#     for dialogue in all_dialogues:
#         if dialogue != "":
#             parts = dialogue.split(":")
#             character = parts[0]
#             line = parts[1]
#             cast[character] = cast.get(character, "") + line
#     return cast

# def character_markov(cast):
#     """return a dictionary with characters as keys and markov chains of their lines as values"""



# def character_chains(input_path):
#     """Return a dictionary with characters as keys and possible next characters as values"""

# def make_play(character_chains, chains):
#     """return a play that mimick the style of the original play"""

    # pick a random character
    # using chains to create a new line for that character
    # choose a next character randomly using charater chain
    # create some restriction to end the loop



input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

#rint input_text

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

retweet()

limit_chars(140)

# run capitalise and punctuate
#print capitalise_punctuate(chains)

#print random_text

# check_characters(input_path)
