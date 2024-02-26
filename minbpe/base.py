""" 
Contains the base Tokenizer class and a few common helper functions. 
The base class also contains the (common) save/load funcitonality.
It would be possible to be a lot mroe strict about the interface and 
e.g. isolating all regex/pattern parts to the RegexTokenizer, but
some concessions are made for simplicity.
"""
import unicodedata

#------------------------------------------------------------------------------
# a few helper functions useful for both BasicTokenizer and RegexTokenizer

def get_stats(ids, counts=None):
    """ 
    Given a list of integers, return a dictionary of counts of consecutive pairs
    Examples: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
    Optionally allows to update an existing dictionary of counts
    """
    counts = {} if counts is None else counts
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair,0) + 1
    return counts


def merge(ids, pair, idx):
    """ 
    In the lsit of integers (ids) replace all consecutive occurences
    of pair with the new integer token idx
    Example: ids = [1, 2, 3, 1, 2], pair=(1,2), idx=4 -> [4, 3, 4]
    """
    newids = []
    i = 0
    while i < len(ids):
        # if not at the very last position AND the pair matches, replace it
        if ids[i]==pair[0] and i<len(ids)-1 and ids[i+1]==pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids


def replace_control_characters(s: str) -> str:
    """ 
    Given a string, replace all the control characters into 
    an escape
    """
    # we don't want to print control characters
    # which distrot the output (e.g., \n or much worse)
    chars = []
    for ch in s:
        # unicodedata.category(ch)[0] will return 'C' if it is a control character
        if unicodedata.category(ch)[0] != 'C':
            chars.append(ch) # this character is ok
        else:
            chars.append(f"\\u{ord(ch):04x}") # escape
    return "".join(chars)


def render_token(t: bytes) -> str:
    """ 
    Given a utf-8 encoding messge, return it's string format
    """
    # Pretty print a toke, escaping control characters
    s = t.decode('utf-8', errors='replace')
    s = replace_control_characters(s)
    return s