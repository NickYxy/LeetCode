__author__ = 'nickyuan'
'''
Given a List of words, return the words that can be typed using letters of alphabet 
on only one row's of American keyboard like the image below.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

#1、用最普通的求交集的办法 34ms
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1 = set('qwertyuiop')
        l2 = set('asdfghjkl')
        l3 = set('zxcvbnm')
        l4=[]
        for word in words:
            w = set(word.lower())
            if l1&w==w:
                l4.append(word)
            elif l2&w==w:
                l4.append(word)
            elif l3&w==w:
                l4.append(word)
        return l4

#2、用正则表达式 29ms
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        import re
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)