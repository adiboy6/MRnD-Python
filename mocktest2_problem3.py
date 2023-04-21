__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
For this problem you have to implement a generator which returns all k digit 
numbers whose sum of digits is n. 

Note that you must not generate the entire solution set at one go (ie) the 
result should be generated on demand (when next is called on generator). This means that 
I can call it with large values of n and k like 1000 and 500 and still 
its use of memory must be modest.

Notes:
1. raise TypeError if n and k are not ints.  
2. if n or k are not positive, raise ValueError 
3. the result numbers must be yield'ed in increasing order. 
4. you are free (encouraged :-) ) to define additional sub-routines as you see fit as long as you do not   
   violate the generator semantics given above

Examples:
 for n = 2 and k = 2, the generator must yield 11, 20 in that order
 for n = 4 and k = 2, the generator must yield 13, 22,31,40 in that order
 
Note that numbers starting with 0 are not valid For e.g. 02 is not a valid 2 digit number
'''

#Implement this generator.
def kdigitnums(n, k):
    """
    This is a generator returns all k digit numbers whose sum is n. The numbers are yielded in
    increasing order
    """
    if (type(n).__name__ != 'int' or type(k).__name__ != 'int'):
        raise TypeError
    if(n<0 or k<0):
        raise ValueError
    first=1
    last=n-first
    num=[0]*k
    while first<=last:
        num[0]=first
        num[-1]=last
        if(sum(num)==n):
            num[0] = str(first)
            num[-1] = str(last)
            num[1:-1]=str(num[1:-1])
            yield int("".join(num))
        first+=1
        last-=1

# write more tests
def test_kdigitnums():
    assert [11, 20] == list(kdigitnums(2,2))
