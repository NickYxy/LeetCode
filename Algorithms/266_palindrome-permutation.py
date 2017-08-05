__author__ = 'nickyuan'
'''
Given a string, determine if a permutation of the string could form a palindrome.

For example, "code" -> False, "aab" -> True, "carerac" -> True.
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        d = Counter(s)
        if len(s) == 1:
            return True
        elif len(s) % 2 == 0:
            if len(set(s)) * 2 == len(s) and (d[c] % 2 == 0 for c in s):
                return True
            else:
                return False
        else:
            if len(set(s)) * 2 == len(s) + 1:
                return True
            else:
                return False


'''
回文字符串分两种，一种是奇数，一种是偶数
用set方法去重，然后比较长度
但是如果多余的是本来就有的，就无法得到正确解答,需要让每一个元素的次数都为偶数
此方法不可行。

'''


class Solution1(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        evenCount = 0
        oddCount = 0
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for k in d:
            if d[k] % 2 == 1:
                oddCount += 1
            else:
                evenCount += 1

        if len(s) % 2 == 1:
            if oddCount == 1:
                return True
        else:
            if oddCount == 0:
                return True
        return False

from collections import Counter
a = Solution()
print(a.canPermutePalindrome('abcbaa'))
print(Counter('abcbaa'))