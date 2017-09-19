__author__ = 'nickyuan'
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited 
such that you cannot load all elements into the memory at once?
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

    def intersect1(self, nums1, nums2):
        from collections import Counter
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())

'''
What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at
once?
If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, 
read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, 
sort them individually (external sort), 
then read 2 elements from each array at a time in memory, record intersections.
'''