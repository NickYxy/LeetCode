__author__ = 'nickyuan'
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        for i in s:
            s1.append(i)
        s1.reverse()
        return ''.join(s1)


class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        s1.reverse()
        return ''.join(s1)
