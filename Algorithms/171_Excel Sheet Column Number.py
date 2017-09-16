__author__ = 'nickyuan'
'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

'''class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))

'''

s = 'ZB'
s1 = map(lambda x: ord(x) - ord('A') + 1, s)
s2 = []
for i in s1:
    s2.append(i)
print(s2)
from functools import reduce

print(reduce(lambda x, y: x * 26 + y, [1]))
f = lambda x, y: x * 26 + y
print(f(1,2))
