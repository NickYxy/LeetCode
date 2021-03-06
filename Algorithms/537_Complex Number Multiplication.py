__author__ = 'nickyuan'
'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a 
and b will both belong to the range of [-100, 100]. And the output should be also in this form.
'''
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = int(a.split('+')[0])
        a2 = int(a.split('+')[1][:-1])
        b1 = int(b.split('+')[0])
        b2 = int(b.split('+')[1][:-1])
        return str((a1 * b1 - a2 * b2)) + '+' + str((a1 * b2 + a2 * b1)) + 'i'

'''
唯一的难点就是a和b的处理，用切片就可以把两个常数分解出来
'''