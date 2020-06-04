"""Anagram Solving tools"""
from itertools import combinations
import Dic_Build as DB

Master_Dic = DB.load_obj('MasterDictionary')

def Countdown_solver(string, *min_len):
    """From a string Find_words generates a dictionary of all possible words
    down to a minimum  length (default 3)"""
    if min_len:
        min_len = min_len[0]
    else:
        min_len = 3

    max_len = len(string)
    output = {x : set() for x in range(min_len, max_len + 1)}

    for k in output:
        combos = combinations(string, k)
        for combo in combos:
            look_up = DB.read_dict(Master_Dic, DB.word_splitter(''.join(combo)))
            if look_up is not None:
                output[k].update(look_up)

    return output
'''
def Exact_anagram_solver(string):
    """Returns a word or phrase that is an exact match to the string."""
    def drill_down(string, path):
        if string == '':
            return path
        words = Countdown_solver(string, 1)
        unpack = [j for i in [list(words[i]) for i in words] for j in i]
        for word in words:
'''           
        
    