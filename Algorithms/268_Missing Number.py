__author__ = 'nickyuan'
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = (len(nums)) * (len(nums) + 1) / 2
        return s - sum(nums)

    def missingNumber1(self, nums):
        from functools import reduce
        from operator import xor
        return reduce(xor, nums + range(len(nums) + 1))

    '''
Xor-ing with O(1) space
Saw this from ts before. Xoring 0..n results in [n, 1, n+1, 0][n % 4]. 
You can also spot the pattern by looking at xors of such ranges, and it's easy to explain as well.
    '''

    def missingNumber2(self, nums):
        from functools import reduce
        from operator import xor
        n = len(nums)
        return reduce(xor, nums) ^ [n, 1, n + 1, 0][n % 4]
