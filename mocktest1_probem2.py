__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''

def smallest_palindrome(word):
    if(type(word).__name__!='str'):
        raise TypeError
    if(word==None or word.lower()==(word[::-1]).lower()):
        return word
    if(not word.isalpha()):
        raise ValueError
    i,j=1,len(word)%2
    while (word[-i:])[::-1] in word[:-i].lower() or (word[-i:])[::-1] in word[:-i]:
        i += 1
    if (j == 0 and (i != 1) and (word[-i] == word[i + j] or word[-i] == word[i + 2])):
        k = abs(len(word[:-i]) - len(word[-i + j + 1:]))
        return word + (word[:k - j])[::-1].lower()
    elif (j == 1 and (i != 1) and (word[-i] == word[i + j] or word[-i] == word[i + 3])):
        k = abs(len(word[:-i]) - len(word[-i + j:]))
        return word + (word[:k])[::-1].lower()
    else:
        return word + (word[:-i])[::-1].lower()


# write your own tests
def test_smallest_palindrome():
    assert "RORaror" == smallest_palindrome("RORar")
    assert "dudedud" == smallest_palindrome("duded")
    assert "RoTator" == smallest_palindrome("RoTa")