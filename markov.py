from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    return contents

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    splitted_words = text_string.split()
    chains = {}

    value_list = []
    for each_word in range(len(splitted_words)- 2):
        third_word = splitted_words[each_word + 2]
        key_tuple = splitted_words[each_word], splitted_words[each_word+1]
        

        if key_tuple in chains:
            old_list = chains.get(key_tuple)
            chains[key_tuple] = old_list + [third_word]
        else:
            value_list.append(third_word)
            chains[key_tuple] = value_list



    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
