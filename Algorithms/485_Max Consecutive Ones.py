__author__ = 'nickyuan'
'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        cnt = 0
        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
                res.append(cnt)
        return max(res)
'''
这道题让我们求最大连续1的个数，不是一道难题。我们可以遍历一遍数组，
用一个计数器cnt来统计1的个数，方法是如果当前数字为0，那么cnt重置为0，如果不是0，cnt自增1，然后每次更新结果res即可
'''
s = Solution()
print(s.findMaxConsecutiveOnes([1,1,1,1,1,0,1,1,1,1]))

class Solution1(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
                res = max(cnt,res)
        return res


s1 = Solution1()
print(s1.findMaxConsecutiveOnes([1,1,1,1,1,0,1,1,1,1]))


'''
由于是个二进制数组，所以数组中的数字只能是0或1，
那么连续1的和跟个数相等，所以我们可以计算和，通过加上num，再乘以num来计算，
如果当前数字是0，那么sum就被重置为0，还是要更新结果res
'''
class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum = 0
        for num in nums:
                sum = (sum + num) * num
                res = max(sum,res)
        return res