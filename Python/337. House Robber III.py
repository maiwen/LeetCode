# -*- coding: utf-8 -*-
"""
Created on 2018/7/22 20:43

@author: vincent

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        val2 = self.rob(root.left) + self.rob(root.right)
        return max(val1, val2)

class Solution1:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob_recr(root):
            if not root:
                return 0, 0
            else:
                left_node, left_grand_node = rob_recr(root.left)
                right_node, right_grand_node = rob_recr(root.right)
                return max(left_node+right_node, root.val + left_grand_node+right_grand_node), left_node+right_node
        return max(rob_recr(root))