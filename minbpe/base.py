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
        if id[i]:
            pass