__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].

vowels=['a','e','i','o','u']

def to_custom_base5(number):
    if(type(number).__name__!='int'):
        raise TypeError
    sign=0
    if(number<0):
        number=-number
        sign=1
    l=[]
    while(number):
        l.append(vowels[number%5])
        number=number//5
    if(sign==1):
        return '-'+"".join(l)[::-1]
    return "".join(l)[::-1]


# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):
    if(type(s).__name__!='str'):
        raise TypeError
    if(s==None):
        raise ValueError
    s=s.lower()
    sign=0
    if(s[0]=='-'):
        sign=1
    if(s[0]=='+'):
        sign=2
    s=s.strip(" ")
    if ' ' in s:
        raise ValueError
    num=0
    if(sign!=0):
        pow=len(s[1:])
        s=s[1:]
    else:
        pow = len(s)
    pow-=1
    for i in s:
        num=num+(vowels.index(i))*(5**pow)
        pow-=1
    if(sign==1):
        return -num
    return num

# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "-ia" == to_custom_base5(-10)
    assert "ea" == to_custom_base5(5)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert 10 == from_custom_base5("+ia")
    assert 5 == from_custom_base5("ea")