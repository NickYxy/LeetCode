__author__ = 'nickyuan'
'''
Given a string, you need to reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.


'''
#1 49ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "Let's take LeetCode contest"
        s1 = ''
        for word in s.split():
            word = word[::-1]
            s1 +=  word + ' '
        return s1.strip() #strip()去掉首尾空格

#2 39ms one line python
class Solution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "Let's take LeetCode contest"
        return ''.join(word[::-1] + ' ' for word in s.split()).strip()
        # return ' '.join(x[::-1] for x in s.split())
        # return ' '.join(s.split()[::-1])[::-1]

s2 = Solution1()
s = "Let's take  LeetCode    contest"
print(s2.reverseWords(s))
w3 = "contest   LeetCode  take Let's"


