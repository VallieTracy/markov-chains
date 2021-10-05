"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file):
    """Take file path as string; return text as string. """
    file = open(file)
    big_string = file.read()
    print(big_string)
    big_string = big_string.split()
    print(f"BIG STRING: {big_string}")

    """
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return(big_string)

whole_string = open_and_read_file(sys.argv[1])


def make_chains(string): 

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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
    
    print("HELLO")

    print(string)
    #loop over i, i+1, i+2, staying in range
    string.append(None)

    for i in range(len(string)-2):
        print(string[i], string[i + 1])
        
        if (string[i], string[i + 1]) not in chains.keys():

            chains[(string[i], string[i + 1])] = [string[i + 2]]
            
        else:
            chains[(string[i], string[i + 1])].append(string[i + 2])
            
        
        
        
    #add i+2 to list, becomes end of dict
    #add i, i+1 to dict as tuples
    
    print(chains)

    #sort keys
    

    return chains

our_dict = make_chains(whole_string)
print("This is our real dictionary")
print(our_dict)



def make_text(chains):
    """Return text from chains."""

    words = []

    first_words = rand.choice(chains.keys())
    #pick a key
    words.append(first_words)
    
    #from first words, rand.choice(chains.value(first_words))
    #ask, how to pull dictionary of correct key
    words.append(thatchoice[1])
    
    #pick a value from list
    #pick newe key based on value
    #keep looping

    return ' '.join(words)


  #  input_path = 'green-eggs.txt'

#print(make_text(our_dict))

# Open the file and turn it into one long string
  #  input_text = open_and_read_file(input_path)

# Get a Markov chain
  #  chains = make_chains(input_text)

# Produce random text
  #  random_text = make_text(chains)

  #  print(random_text)
