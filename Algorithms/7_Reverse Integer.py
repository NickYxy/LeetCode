__author__ = 'nickyuan'
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        from operator import le,lt,eq,gt,ge
        if x == 0:
            return 0
        s= -1 if x < 0 else 1
        r=int(str(s*x)[::-1])
        return(r<2**31)*s*r