__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given 2 strings str1 and str2, find out the minimum number of right rotations str1 needs to undergo
to create str2. If is not possible, return -1

Notes:
1. Assume inputs are either None or valid strings
2. Write plain brute force code.
3. result should be -1 if not possible
4. If it is possible then give the 'minimum rotations' required.
5. No need for type checking.
'''

def get_right_rotations(str1, str2):
    i=1
    if(str1==None or str2==None or len(str1)!=len(str2)):
        return -1
    while True:
        if (str1[-i:] + str1[:-i] == str2):
            return i
        if (i == len(str1)):
            return -1
        i += 1

# basic test given, write more tests to ensure correctness.
def test_get_right_rotations():
    assert 3 == get_right_rotations("abcd", "bcda")