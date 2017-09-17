__author__ = 'nickyuan'
'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        s3 = []
        if not s:
            return -1  # s = ''
        if len(s) > 1 and len(Counter(s)) == 1:
            return -1  # s = 'cc'
        for k, v in Counter(s).items():
            if v == 1:
                s3.append(k)
        if len(s3) == 0:
            return -1  # s里不存在单个元素
        for i in range(len(s)):
            if s[i] in s3:
                return i

    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1