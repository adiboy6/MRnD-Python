__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if " either " in sentence and " or " in sentence:
        if sentence.count("or")==1 and sentence.count("either")==1 and sentence.index("either")<sentence.index("or") and (-sentence.index("either")+sentence.index("or"))>7 and sentence.index("either")>0 and sentence.index("or")>0:
            x = sentence.index("either")
            y = sentence.index("or")
            s = sentence[:x - 1]
            t = sentence[x + 6:y - 1]
            return s + t
        else:
            return sentence
    else:
        return sentence


def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "we could either go to a movie or or a hotel" == prune_either_or("we could either go to a movie or or a hotel")
    assert "we could either either go to a movie or or a hotel" == prune_either_or("we could either either go to a movie or or a hotel")
    assert "we could go to a movie a hotel" == prune_either_or("we could go to a movie a hotel")
    assert "we could go or to a movie either a hotel" == prune_either_or("we could go or to a movie either a hotel")
    assert "We can go to a movie" == prune_either_or("We can go either to a movie or to a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
