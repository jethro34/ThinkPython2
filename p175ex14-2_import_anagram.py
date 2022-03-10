# module that imports anagram_sets and provides two new functions:
# store_anagrams should store the anagram dictionary in a “shelf ”;
# read_anagrams should look up a word and return a list of its anagrams.


import dbm
import pickle
import sys

sys.path.insert(1, '/Users/hejtor/PycharmProjects/ThinkPython')

import p148ex120201_anagrams


def store_anagrams(dikt, database):
    """ Stores a dictionary in a database. """

    db = dbm.open(database, 'c')
    for key in dikt:
        db[pickle.dumps(key)] = pickle.dumps(dikt[key])
    db.close()


def read_anagrams(database, wort):
    """ Looks up a word in a database.
        Output: list """

    key = pickle.dumps(p148ex120201_anagrams.alpha_skeleton(wort))
    db = dbm.open(database, 'r')
    temp = pickle.loads(db[key])
    db.close()
    return temp


anagrams = p148ex120201_anagrams.anagram_dict(p148ex120201_anagrams.dict_from_file())
store_anagrams(anagrams, '/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/db_anagrams')
list_of_anagrams = read_anagrams('/Users/hejtor/Library/CloudStorage/OneDrive-Personal/CS/ThinkPython stuff/db_anagrams', 'pear')
print(list_of_anagrams)
