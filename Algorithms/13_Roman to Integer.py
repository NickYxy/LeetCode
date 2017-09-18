__author__ = 'nickyuan'
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
'''
罗马数字采用七个罗马字母作数字： 
I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。

记数的方法： 
1. 相同的数字连写，所表示的数等于这些数字相加得到的数，如 III=3； 
2. 小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 VIII=8、XIII=12； 
3. 小的数字（限于 I、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 IV=4、IX=9； 
4. 在一个数的上面画一条横线，表示这个数增值 1,000 倍。
'''
'''第一种解法：
根据上面说的计数方法的前三条。
对于输入的罗马数字字符串，从后向前扫描，遇到前面数大于等于后面的最大数的时候，相加；
遇到前面数小于后面的最大数的时候，相减。'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        maxDigit = 1
        for i in range(len(s)-1, -1, -1):
            if d[s[i]] >= maxDigit:
                maxDigit = d[s[i]]
                sum += d[s[i]]
            else:
                sum -= d[s[i]]
        return sum