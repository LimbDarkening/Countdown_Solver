""" A Module that can build Dictionary trees and read from them."""
import pickle

def build_dict(Dic, word_ls, word):
    """ A function that builds a nested dictionary recursively, from the
    output of the word_splitter function and the word."""
    if word_ls == []:
        return

    let = word_ls.pop(0)

    if let not in Dic:

        if let == '*':
            Dic[let] = []

        else:
            Dic[let] = {}

    if let == '*':
        Dic[let].append(word)

    build_dict(Dic[let], word_ls, word)

def read_dict(Dic, string):
    """Finds all words that exactly match the string input, in the nested
    Dictionary passed"""
    let = string.pop(0)
    if not Dic.get(let):
        return
    if let == '*':
        return Dic.get('*')

    return read_dict(Dic[let], string)

def word_splitter(word):
    """Returns the string as a list of characters in alphabetical order,
    followed by '*' designating the end of the list"""
    word_ls = sorted(word)
    word_ls.append('*')
    return word_ls

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

if __name__ == "__main__":

    from nltk.corpus import wordnet as wn
    from itertools import chain
    import string

    #Generate word list
    lemmas_in_wordnet = set(chain(*[ss.lemma_names() for ss in wn.all_synsets()]))

    #cleaning the list and sorting duplicates
    punctuation = string.punctuation.replace('_', '')
    Clean = set()

    for lemma in lemmas_in_wordnet:

        no_punc = lemma.translate(str.maketrans('', '', punctuation)).lower()
        no_numbers = no_punc.translate({ord(k): None for k in string.digits})
        lemmas = no_numbers.split('_')
        Clean.update(lemmas)

    #Building the Main Dictionary
    DIC = {}
    count = 0
    for Word in Clean:
        count += 1
        word_ls = word_splitter(Word)
        build_dict(DIC, word_ls, Word)

    print(f'Dictionary built with {count} entries.\n')
    print('Saving Dictionary...\n')
    save_obj(DIC, 'MasterDictiona           ry')
    print('Done')
    