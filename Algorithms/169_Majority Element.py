__author__ = 'nickyuan'
'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c= Counter(nums)
        return c.most_common(1)[0][0]
        #return sorted(num)[len(num)/2]

'''
public class Solution {
    public int majorityElement(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;
            
        }
        return major;
    }
}
'''
'''
# two pass + dictionary
def majorityElement1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num
    
# one pass + dictionary
def majorityElement2(self, nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1 

# TLE
def majorityElement3(self, nums):
    for i in xrange(len(nums)):
        count = 0
        for j in xrange(len(nums)):
            if nums[j] == nums[i]:
                count += 1
        if count > len(nums)//2:
            return nums[i]
            
# Sotring            
def majorityElement4(self, nums):
    nums.sort()
    return nums[len(nums)//2]
    
# Bit manipulation    
def majorityElement5(self, nums):
    bit = [0]*32
    for num in nums:
        for j in xrange(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit if 1, 
            # it means it's a negative number 
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res
            
# Divide and Conquer
def majorityElement6(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = self.majorityElement(nums[:len(nums)//2])
    b = self.majorityElement(nums[len(nums)//2:])
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums)//2]
    
# the idea here is if a pair of elements from the
# list is not the same, then delete both, the last 
# remaining element is the majority number
def majorityElement(self, nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:
            count += 1
        elif count == 0:
            cand, count = num, 1
        else:
            count -= 1
    return cand
'''