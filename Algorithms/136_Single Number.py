__author__ = 'nickyuan'
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # from collections import Counter
        # return min(Counter(nums))
        return 2 * sum(set(nums)) - sum(nums)


s = Solution()
print(s.singleNumber([4, 2, 2, 4, 3]))

'''
因为A XOR A = 0，且XOR运算是可交换的，于是，对于实例{2,1,4,5,2,4,1}就会有这样的结果：

(2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5
'''


def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        #dict = {4:2,2:2,3:1}
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber2(self, nums):
    from collections import Counter
    dic = Counter(nums)
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber3(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res


from functools import reduce


def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)


import operator


def singleNumber(self, nums):
    return reduce(operator.xor, nums)


a = [1, 2, 3]
b = (1, 2, 3)
print(sum(a))
print(sum(b))
c = [1, 1, 2, 2, 3]
print(list(b))
