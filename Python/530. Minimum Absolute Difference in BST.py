# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:19:48 2018

@author: Administrator

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDiff = float('inf')
        self.prenode = None
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            if self.prenode:
                self.minDiff = min(self.minDiff, root.val - self.prenode.val)
            self.prenode = root
            inorder(root.right)
        inorder(root)
        return self.minDiff
