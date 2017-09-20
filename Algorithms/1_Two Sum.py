__author__ = 'nickyuan'
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
用暴力解法，时间复杂度是n的平方，但是空间复杂度是1，因为没有开辟新空间
'''


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[j] == nums[i]:
                    return [i, j]


'''
推荐用hash，也就是字典来做,hashtable寻址是1的时间，所以很方便
'''
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        for i, num in enumerate(nums):
            if target - num in dict and dict[target-num] != i:
                return [i,dict[target-num]]

'''
上面的那个还是遍历，如果不遍历所有的元素呢？
'''
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict and dict[target-num] != i:
                return [i,dict[target-num]]
            else:
                dict[num] = i