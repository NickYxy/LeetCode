__author__ = 'nickyuan'
'''
617_Merge Two Binary Trees
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1 First solution:

'''
Let's create a recursive solution.

If both trees are empty then we return empty.
Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
The right child is similar.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans


# 2 Recursive
class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        if t1:
            v1, L1, R1 = t1.val, t1.left, t1.right
        else:
            v1, L1, R1 = 0, None, None
        if t2:
            v2, L2, R2 = t2.val, t2.left, t2.right
        else:
            v2, L2, R2 = 0, None, None

        node = TreeNode(v1 + v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node
