__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import unit6utils
import string

def anagram_sort(source, destination):
    f = open(source, "r")
    text = f.read()
    f.close()
    filelist = text.split("\n")
    wordlist = []
    for i in filelist:
        if ('#' not in i) and (i != ''):
            wordlist.append(i)
    anagrams={}
    for i in wordlist:
        j=i.lower()
        for k in anagrams:
            if set(j)==set(k) and len(j)==len(k):
                anagrams[k].append(i)
                break
        else:
            anagrams[j] = []
            anagrams[j].append(i)
    l=[]
    for i in anagrams:
        anagrams[i]=sorted(anagrams[i],key=str.lower)
        l.append(anagrams[i])
    l=sorted(sorted(l,key=lambda x:x[0].lower()),key=len,reverse=True)
    s=""
    for i in l:
        for j in i:
            s+=j+'\n'
    f=open(destination,"w")
    f.write(s)
    f.close()

if __name__ == "__main__":
    fin=sys.argv[1]
    if('.txt' not in fin):
        raise NameError
    try:
        fin=unit6utils.get_input_file(fin)
        fop = unit6utils.get_input_file(fin[:-4]+"-results.txt")
        anagram_sort(fin,fop)
    except:
        print("There's an error")
    else:
        print("Code run sucessfully")
    #sys.exit(main())