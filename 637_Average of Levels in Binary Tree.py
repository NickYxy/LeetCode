__author__ = 'nickyuan'
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []

        def dfs(node, depth=0):
            if node:
                if len(ans) <= depth:
                    ans.append([0, 0])
                ans[depth][0] += node.val
                ans[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)
        return [s / float(c) for s, c in ans]


a = [[3, 1], [29, 2], [22, 2]]
print([s / float(c) for s, c in a])
