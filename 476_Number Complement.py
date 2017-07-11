__author__ = 'nickyuan'
'''
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.
'''
#1、这是一个补位的问题
# Flip bit by bit.
# class Solution(object):
#     def findComplement(self, num):
#         i = 1
#         while num >= i:
#             num ^= i
#             i <<= 1
#         return num
# Find the bit length (say L) and flip num by num ^ 11...1 (L ones).
#     def findComplement(self, num):
#         return num ^ ((1<<num.bit_length())-1)
# Again find the bit length first.
#     def findComplement(self, num):
#         return num ^ ((1 << len(bin(num)) - 2) - 1)
# def findComplement(self, num):
#         return num ^ ((2<<int(math.log(num, 2)))-1)
# We can also flip num first (including the leading zeros) using ~num and then get the last L bits by & 11...1 (L ones).
#
# For example,
#
#     def findComplement(self, num):
#         return ~num & ((1<<num.bit_length())-1)

#2、可以考虑使用位移运算符<<
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num