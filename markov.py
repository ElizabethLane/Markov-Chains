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
    #Defining a variable splitted_words that is equal to a list of the words in the string.
    chains = {}
    # Creates an empty dictionary

    value_list = []
    #Creates an empty list
    for i in range(len(splitted_words)- 2):
    # loops through list of numbers two less than the last index in the 
    # splitted words       
        third_word = splitted_words[i + 2]
        #Defines a new variable third_word that binds a single word in the splitted
        #words list at an index +2 from the iterated word

        key_tuple = splitted_words[i], splitted_words[i+1]
        # Creates a variable bound to a tuple where the key is stored
        # The key is consecutive iterated words in splitted words

        if key_tuple in chains:
            old_list = chains.get(key_tuple)
            chains[key_tuple] = old_list + [third_word]

        else:
            chains[key_tuple] = [third_word]



    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""


    random_key = choice(chains.keys())
    key_tuple = [random_key[0], random_key[1]]
    markov_words = "" 

    
    while random_key in chains:
        random_word = choice(chains[random_key])
        key_tuple.append(random_word)
        random_key = (random_key[1], random_word)
        markov_words = markov_words + " " + random_word


    return markov_words
    




input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
