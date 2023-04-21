__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys

def pigLatin(word):
    k=len(word)
    if(word[-1]==',' or word[-1]=='.'):
        k=-1
    caps=[0]*len(word[:k])
    for i in range(len(word[:k])):
        if word[i].isupper():
            caps[i]=1
    ind=0
    for i in range(len(word[:k])):
        if (word[i]).lower() in set('aeiou'):
            ind=i
            break
    s=word[ind:k]+word[:ind]
    finword=""
    for i in range(len(s)):
        if caps[i]:
            finword+=s[i].upper()
        else:
            finword += s[i].lower()
    if k!=len(word):
        s=finword+'ay'+word[-1]
    else:
        s = finword + 'ay'
    return s
if __name__ == "__main__":
    sentence=sys.argv[1]
    s=sentence.split()
    final_Sentence=[]
    for i in s:
        final_Sentence.append(pigLatin(i))
    sentence=" ".join(final_Sentence)
    print(sentence)
    #sys.exit(main())