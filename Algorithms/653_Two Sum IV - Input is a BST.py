__author__ = 'nickyuan'
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST 
such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        r = [root]
        s = set()
        for i in r:
            if k - i.val in s:return True
            s.add(i.val)
            if i.left:r.append(i.left)
            if i.right:r.append(i.right)
        return False



class Solution1(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        a = set()
        self.f = False
        def dfs(root, k):
            if not root:
                return
            if root.val not in a:
                a.add(k - root.val)
            else:
                self.f = True
            dfs(root.left, k)
            dfs(root.right, k)
        dfs(root, k)
        return self.f