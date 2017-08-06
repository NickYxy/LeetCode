__author__ = 'nickyuan'
'''
Given a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to the original key plus sum of all keys 
greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root

        # root.val = root.val + root.left if root.left > root.val + root.right if root.right > root.val
        # root.left = root.left + root.val if root.val > root.left + root.right if root.right > root.left
        # root.right = root.right + root.left if root.left > root.right + root.val if root.val > root.right
        # return root
