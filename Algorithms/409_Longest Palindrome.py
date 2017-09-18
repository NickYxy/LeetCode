__author__ = 'nickyuan'
'''
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        count = []
        if len(set(s)) == 1:
            return len(s)
        elif s is None:
            return 0
        elif len(set(s)) == len(s):
            return 1
        else:
            for k, v in d.items():
                if v >= 2:
                    count.append(v)
            if sum(count) % 2 != 0:
                return sum(count)
            elif max(map(lambda x:x % 2, count)) % 2 == 0 and sum(count) < len(s):
                return sum(count) + 1
            elif max(map(lambda x:x % 2, count)) % 2 == 0 and sum(count) == len(s):
                return sum(count)
            else:
                return sum(count)
这是错误的！
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        dict = {}
        count = 0
        for i in range(len(s)):
            if s[i] in dict:
                dict.pop(s[i])
                count += 1
            else:
                dict.update({s[i]:i})
        if dict:
            return count * 2 + 1
        return count * 2

'''
用字典的思路来解决，abbccd
'''

'''
或者使用python里的位计算
I count how many letters appear an odd number of times. 
Because we can use all letters, except for each odd-count letter we must leave one, 
except one of them we can use.

Python:

def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
'''
