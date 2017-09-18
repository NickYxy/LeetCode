__author__ = 'nickyuan'
'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, 
so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(s, rank)).get, nums)

'''
要搞清楚map、zip、filter、reduce等函数的用法
zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。具体意思不好用文字来表述，直接看示例：

1.示例1：

复制代码
x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]

xyz = zip(x, y, z)

print xyz
复制代码
运行的结果是：

[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''