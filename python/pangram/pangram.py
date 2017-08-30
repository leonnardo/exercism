from string import ascii_lowercase

def is_pangram(text):
    # learning more about sets!
    # set <= other: <= operator tests if every element in set 
    # is in other set
    return set(ascii_lowercase) <= set(text.lower())
