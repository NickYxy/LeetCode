__author__ = 'nickyuan'
'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
'''
'''
enumerate 用来同时获取索引和元素
这里用了双重循环，复杂度是n*n*len
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_val = ''
        min_key = 10000
        l = []
        for k1,v1 in enumerate(list1):
            for k2,v2 in enumerate(list2):
                if v1 == v2:
                    key = k1 + k2
                    if key <= min_key:
                        min_key = key
                        min_val = v1
                        l.append(min_val)
        return l

'''
所以，第一是要减掉一层循环，这里考虑用字典的get，因为字典get采用的是hashtable，复杂度是O(1)
'''
class Solution1(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {v:k for k, v in enumerate(list1)}
        min_val = ''
        min_key = 10000
        l = []
        for k1, v1 in enumerate(list2):
            k2 = dic.get(v1, min_val)
            if k1 + k2 <= min_key:
                l.append(v1)

        return l
